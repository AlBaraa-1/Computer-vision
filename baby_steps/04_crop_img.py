import cv2
import os

img_path = os.path.join('computer-vision/baby_steps/assets', 'test.png')

img = cv2.imread(img_path)

# display the original image
cv2.imshow('Original Image', img)

# crop the image - (y1:y2, x1:x2)
cropped_img = img[50:200, 200:350]

cv2.imshow('Cropped Image', cropped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
