##@ entrypoint
##@ next: grayscale.py

import cv2

img = cv2.imread("assets/sample.jpg")

cv2.imshow("Image", img)

cv2.waitKey(0)
