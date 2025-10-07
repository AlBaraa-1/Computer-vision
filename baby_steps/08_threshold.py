import cv2
import os


"""
# Simple Thresholding
img1 = cv2.imread('computer-vision/baby_steps/assets/bear.png')
img1 = cv2.resize(img1, (1000, 600))
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

ret , img1 = cv2.threshold(img1, 190, 255, cv2.THRESH_BINARY)

cv2.imshow('image', img1)
cv2.waitKey(0)
"""

# Adaptive Thresholding
img2 = cv2.imread('computer-vision/baby_steps/assets/image.png')
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(img2, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30)

cv2.imshow('image', img2)
cv2.imshow('thresh', thresh)
cv2.waitKey(0)
