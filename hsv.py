##@ next: smoothing.py
##@ prev: blur.py

import cv2

img = cv2.imread("assets/sample.jpg")

# blur
#? need to blur the image before grayscale
img_blur = cv2.GaussianBlur(img, (13, 13), 3)

# grayscale
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)
#? cant use this grayscale image to generate img_hsv
# but we can convert img_gray to COLOR_GRAY2BGR
# so it can be used to generate hsv
img_gray = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

# HSV
# How humans perceives the color
img_hsv = cv2.cvtColor(img_blur, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", img_hsv)

cv2.waitKey(0)
