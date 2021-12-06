# ML-Zoomcamp-Capstone-Project

## Problem & Objective
In this project, I created a deep learning model to classify images to be animal crossing or doom related. This model probably doesn't have any real world usage, but it's fun, so yeah. The dataset can be found [here](https://www.kaggle.com/andrewmvd/doom-crossing?rvi=1).

## How to Use this Model on Docker
1. Clone this repo to your local machine
2. cd into the directory and create the docker image using
```docker
docker built -t animal-doom .
```
3. Run the image by using
```docker
docker run -it -p 8080:8080 animal-doom:latest
```
4. Run the test.py script with the desire image url, the default image is the following.
![image](https://user-images.githubusercontent.com/20444505/144915447-cfaae0f4-ca78-4828-b20b-eae04b093d2c.png)
