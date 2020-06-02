'''
USAGE:
python hog_detector_vid.py --input ../input/video1.mp4 --output ../outputs/video1_slow.mp4 --speed slow
python hog_detector_vid.py --input ../input/video1.mp4 --output ../outputs/video1_fast.mp4 --speed fast
'''

import cv2 
import time
import argparse
import os

# construct the argument parser and parse the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='../input/video1.mp4', 
                    help='path to the inout video file')
parser.add_argument('-o', '--output', required=True, help='path to save the output video file')
parser.add_argument('-s', '--speed', default='yes', choices=['fast', 'slow'],
                    help='whether to use fast or slow detector')
args = vars(parser.parse_args())

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cap = cv2.VideoCapture(args['input'])

if (cap.isOpened() == False):
    print('Error while trying to play video. Plese check again...')

# get the frame width and height
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

# keep a minimum frame size for accurate predictions
if frame_width < 400: # if image width < 400
        frame_width = 400
        ratio = frame_width / float(frame_width) # find the width to height ratio
        frame_height = int(frame_width * ratio)

# similarly reduce frame size when too big
if frame_width > 1200: # if image width < 400
        frame_width = 640
        ratio = frame_width / float(frame_width) # find the width to height ratio
        frame_height = int(frame_width * ratio)

# define codec and create VideoWriter object
out = cv2.VideoWriter(args['output'], cv2.VideoWriter_fourcc(*'mp4v'), 30, (frame_width, frame_height))

frame_count = 0
total_fps = 0
total_weights = 0
# read until end of video
while(cap.isOpened()):
    # capture each frame of the video
    ret, frame = cap.read()
    if ret == True:
        start_time = time.time()
        
        frame = cv2.resize(frame, (frame_width, frame_height))

        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if args['speed'] == 'fast':
            rects, weights = hog.detectMultiScale(img_gray, padding=(4, 4), scale=1.02)
        elif args['speed'] == 'slow':
            rects, weights = hog.detectMultiScale(img_gray, winStride=(4, 4), padding=(4, 4), scale=1.02)

        for i, (x, y, w, h) in enumerate(rects):
            if weights[i] < 0.13:
                continue
            if weights[i] < 0.3 and weights[i] > 0.13:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            if weights[i] < 0.7 and weights[i] > 0.3:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (50, 122, 255), 2)
            if weights[i] > 0.7:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(frame, 'High confidence', (10, 15), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.putText(frame, 'Moderate confidence', (10, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (50, 122, 255), 2)
        cv2.putText(frame, 'Low confidence', (10, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

        frame_write_name = args['input'].split('/')[-1].split('.')[0]
        cv2.imwrite(f"../outputs/frames/{args['speed']}_{frame_write_name}_{frame_count}.jpg", frame)
        
        # Measure elapsed time for detections
        end_time = time.time()
        fps = 1 / (end_time - start_time)
        # print(f"{fps:.3f} FPS")
        # add to total FPS
        total_fps += fps
        # add to total number of frames
        frame_count += 1
        cv2.imshow("Preview", frame)
        out.write(frame)
        # press `q` to exit
        wait_time = max(1, int(fps/4))
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break

    else:
        break

avg_fps = total_fps / frame_count
print(f"Average FPS: {avg_fps:.3f}" )

# release VideoCapture()
cap.release()

# close all frames and video windows
cv2.destroyAllWindows()