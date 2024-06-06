This is my Major Project of my B Tech I used YOLOv8s Algorithm to create a Deep Learning CNN model of my own to detect ,read and store the numberplate sequence of every four wheeler vehicle passing thorough the live feed.

We are using the small scale model YOLOv8 algorithm.
Our Dataset contains 1816 files which are divided into Train,Valid and Test dataset in 70%,20% and 10% ratio.

the train.py file is used to train the model

the data.yaml file contains all the metadata regarding the training dataset

yolov8s.pt is the yolo model which will be used to train our own model

best.pt is the model generated after the tedious training process is complete

main.py file is used to run a process and use the model to detect license plates from video input or live camera feed which can be controlled using a parameter change in the program

Sample Output: https://drive.google.com/file/d/1iUwK8E7EVKypUbduXqQOlsMEJ6j_IU3O/view?usp=sharing
