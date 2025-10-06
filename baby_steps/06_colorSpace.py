import cv2
import os

img = cv2.imread(os.path.join('computer-vision/baby_steps', 'test.png'))

# convert the image to different color spaces
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lab_img = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

cv2.imshow('Original Image', img)
cv2.imshow('Grayscale Image', gray_img)
cv2.imshow('HSV Image', hsv_img)
cv2.imshow('Lab Image', lab_img)

cv2.waitKey(0)
cv2.destroyAllWindows()

