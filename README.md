This is our Major Project of B.Tech where we've used YOLOv8s Algorithm to create a Deep Learning CNN Model to detect, read and store the numberplate sequence of four wheeler vehicles passing thorough the live feed.

We are using the small scale, efficient and robust model - YOLOv10 algorithm for detecting the number plates.
Our Dataset constitutes of 5086 files(images) which are divided into Train, Validation and Test dataset in 7:2:1 ratio respectively.

the train.py file is used to train the model

the data.yaml file contains all the metadata regarding the training dataset

yolov8s.pt is the yolo model which will be used to train our own model

best.pt is the model generated after the tedious training process is complete

main.py file is used to run a process and use the model to detect license plates from video input or live camera feed which can be controlled using a parameter change in the program

Sample Output: https://drive.google.com/file/d/1iUwK8E7EVKypUbduXqQOlsMEJ6j_IU3O/view?usp=sharing

We'll  appreciate any feedback from your end.
Thank you!
