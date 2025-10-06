import cv2
import os

# get the path of the video
video_path = os.path.join('computer-vision/baby_steps', 'test.mp4')
print(video_path)

# read the video 
video = cv2.VideoCapture(video_path)

# display the video in a window
ret = True # ret is boolean to know that we have frames with no error
while ret:
    ret, frame = video.read()

    if ret:
        cv2.imshow('video', frame)
        if cv2.waitKey(30) & 0xFF == ord('q'): # press 'q' to quit
            break

# release the video capture object and close all windows
video.release()
cv2.destroyAllWindows()