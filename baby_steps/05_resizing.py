import cv2
import os

img_path = os.path.join('computer-vision/baby_steps', 'test.png')
img = cv2.imread(img_path)

# get the size of the image
print(f'Image shape:         {img.shape}')

# resize the image to half the size
resized_img = cv2.resize(img, (int(1486/2), int(833/2))) # (width, height)

# get the size of the resized image
print(f'Resized image shape: {resized_img.shape}')


cv2.imshow('Image', img)
cv2.imshow('Resized Image', resized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
