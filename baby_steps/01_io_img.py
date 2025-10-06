import cv2
import os

# get the path of the image
img_path = os.path.join('computer-vision/baby_steps', 'test.png')

# read the image
img = cv2.imread(img_path)

# save the image to a new file - optional
cv2.imwrite('output.png', img)

# display the image in a window
cv2.imshow('image', img)
cv2.waitKey(0)
