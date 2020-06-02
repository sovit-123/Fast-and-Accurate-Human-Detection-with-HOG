# Fast-and-Accurate-Human-Detection-with-HOG



* This project used OpenCV HOG people detector to build an accurate and fast enough implementation to detect people in images and videos.



## <u></u>



## <u>The Project Structure</u>

```
├───input
        people1.jpg
        people2.jpg
        people3.jpg
        video1.mp4
        video2.mp4
        video3.mp4
        video4.mp4
├───outputs
│   └───frames
└───src
        hog_detector.py
        hog_detector_vid.py
```

* After cloning the repository, you need to create the `input` and `outputs` folder.
* You can find all the data in the input folder in the [References](#References) section.



## <u>Executing the Python Files</u>

* `hog_detector.py`: Execute this file from within the `src` folder in the terminal. This detects the people in images inside the `input` folder.
* `hog_detector_vid.py`:  Execution details:
  * `python hog_detector_vid.py --input ../input/video1.mp4 --output ../output/video1_slow.mp4 --speed slow`: Use this execution command to run slow but accurate video detection algorithm.
  * `python hog_detector_vid.py --input ../input/video1.mp4 --output ../output/video1_fast.mp4 --speed fast`: Use this command to execute a little bit less accurate but fast video detection algorithm.



## <u>References</u>

* **Credits and Citations**:
  * `input/people1.jpg`: Image by <a href="https://pixabay.com/photos/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438393">Free-Photos</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=438393">Pixabay</a>.
    * Link: https://pixabay.com/photos/urban-people-crowd-citizens-438393/.
  * `input/people2.jpg`: http://www.cbc.ca/natureofthings/content/images/episodes/pompeiipeople_listical.jpg.
  * `input/people3.jpg`: https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.us0yaLcftx1jwMQ-tcw34gHaEU%26pid%3DApi&f=1.
  * `input/video1.mp4`: https://pixabay.com/videos/people-commerce-shop-busy-mall-6387/.
  * `input/video2.mp4`: https://pixabay.com/videos/pedestrians-road-city-cars-traffic-1023/.
  * `input/video3.mp4`: Video by <a href="https://pixabay.com/users/surdumihail-3593622/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6096">Mihai Surdu</a> from <a href="https://pixabay.com/?utm_source=link-attribution&amp;utm_medium=referral&amp;utm_campaign=image&amp;utm_content=6096">Pixabay</a>.
    * Link: https://pixabay.com/videos/park-old-people-people-old-senior-6096/.
  * `input/video4.mp4`:
    * Link: https://www.pexels.com/video/athletes-warming-up-1585619/.
  * `input/video5.mp5`: 
    * Link: https://www.youtube.com/watch?v=NyLF8nHIquM.
