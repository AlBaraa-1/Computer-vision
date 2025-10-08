import cv2


img = cv2.imread('computer-vision/baby_steps/assets/contour_test.png')
img = cv2.resize(img, (750, 750))

cv2.imshow('original', img)

# convert to grayscale and threshold
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY_INV)

# find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    if cv2.contourArea(cnt) > 100:

        # print the area of the borders
        print(cv2.contourArea(cnt))

        # highlight edges 
        cv2.drawContours(img, cnt, -1,(0, 0, 255), 2)

        # get bounding box
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 1)

cv2.imshow('img', img)
cv2.waitKey(0)