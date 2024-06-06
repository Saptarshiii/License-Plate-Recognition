from ultralytics import YOLO
import cv2
model=YOLO('best.pt')
video='Input.mp4'
cap=cv2.VideoCapture(video)
rate=True
while rate:
    rate,frame=cap.read()
    if rate:
        results=model.track(frame,persist=True)
        cv2.rectangle
        cv2.putText
        frame1=results[0].plot()
        cv2.imshow('video',frame1)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()