'''
NOTE:
This python script is for building a custom person detector using HOG features.
'''

import cv2
import glob as glob
import numpy as np

from skimage import feature, exposure
from sklearn.svm import LinearSVC

def get_hog_features():
    images = []
    labels = [1, 2, 1]

    image_paths = glob.glob('../input/*.jpg')

    for i, image_path in enumerate(image_paths):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (128, 256))
        img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (hog_feature, hog_image) = feature.hog(img_gray, orientations=9,
                                                pixels_per_cell=(8, 8),
                                                cells_per_block=(2, 2), 
                                                visualize=True)
        # rescale image to 0. ... 255.
        img_rescaled = exposure.rescale_intensity(hog_image, out_range=(0, 255))
        # cv2.imshow('Image', img_rescaled)
        cv2.imwrite(f"../outputs/image{i}.jpg", img_rescaled)
        # cv2.waitKey(0)

        images.append(hog_feature)
        # labels.append()

    return images, labels

def train_linear_svm(images, labels):
    svm = LinearSVC(random_state=42, tol=0.0001)
    model = svm.fit(images, labels)

    return model

def get_bbox_detections(model):
    image = cv2.imread('../input/people1.jpg')
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    model.set

    rects, weights = model.detectMultiScale(img_gray)

    for i, (x, y, w, h) in enumerate(rects):
        if weights < 0.5:
            continue
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('image', image)
    cv2.waitKey(0)

images, labels = get_hog_features()
model = train_linear_svm(images, labels)
get_bbox_detections(model)