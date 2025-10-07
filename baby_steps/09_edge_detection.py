import cv2


img = cv2.imread('computer-vision/baby_steps/assets/edge_detection.png')

img_edge = cv2.Canny(img, 100, 200)

cv2.imshow('image', img)
cv2.imshow('edges', img_edge)
cv2.waitKey(0)

# code for interactive edge detection tuning
"""
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

cv2.namedWindow("edges")

def nothing(x): pass

cv2.createTrackbar("Lower", "edges", 50, 500, nothing)
cv2.createTrackbar("Upper", "edges", 150, 500, nothing)

while True:
    lo = cv2.getTrackbarPos("Lower", "edges")
    hi = cv2.getTrackbarPos("Upper", "edges")
    if lo > hi:  # keep order sensible
        hi = lo + 1
        cv2.setTrackbarPos("Upper", "edges", hi)
    edges = cv2.Canny(gray, lo, hi)
    vis = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    vis[edges != 0] = (0, 255, 0)
    cv2.imshow("edges", edges)
    cv2.imshow("overlay", vis)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
"""