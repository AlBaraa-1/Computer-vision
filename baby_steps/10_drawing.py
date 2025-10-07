import cv2

img = cv2.imread('computer-vision/baby_steps/assets/white_board.png')

cv2.imshow('original', img)
print(img.shape)

# Draw a line | start,      end,      color(BGR), thickness
cv2.line(img, (300, 350), (200, 200), (255, 0, 0), 3)

# Draw a rectangle| top-left, bottom-right
cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 3)

# Draw a circle | center, radius
cv2.circle(img, (350, 350), 50, (0, 0, 255), 3)

# Draw text     | text,           position,         font,     font-scale, color, thickness
cv2.putText(img, 'Hello World!', (225, 230), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()