import cv2
import os


img = cv2.imread('computer-vision/baby_steps/assets/blure_test.png')
img = cv2.resize(img, (600, 400))

# Apply different blurring techniques
k_size = 5 # It decides how to combine surrounding pixels to produce a new pixel value
img_blured = cv2.blur(img, (k_size, k_size))
img_gaussian = cv2.GaussianBlur(img, (k_size, k_size), 0)
img_median = cv2.medianBlur(img, k_size)

cv2.imshow('image', img_blured)
cv2.imshow('image_gaussian', img_gaussian)
cv2.imshow('image_median', img_median)
cv2.waitKey(0)
