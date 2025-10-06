import cv2
import os

# read webcam
webcam = cv2.VideoCapture(0)

# view webcam
while True:
    ret, frame = webcam.read()

    cv2.imshow('webcam', frame)
    if cv2.waitKey(30) & 0xFF == ord('q'): # press 'q' to quit
        break

# release the webcam and close all windows
webcam.release()
cv2.destroyAllWindows()