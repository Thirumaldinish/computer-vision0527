import cv2
import numpy as np
video_path = r"C:\Users\ADMIN\Downloads\SampleVideo_1280x720_1mb.mp4"
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error opening video file")
else:
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Frame', frame)
            if cv2.waitKey(250) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
cv2.destroyAllWindows()
