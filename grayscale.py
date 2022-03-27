##@ next: blur.py
##@ prev: helloworld.py

import cv2

img = cv2.imread("assets/sample.jpg")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Image", img_gray)

cv2.waitKey(0)
