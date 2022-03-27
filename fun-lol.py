##@ next: 
##@ prev: smoothing.py

import cv2
import numpy as np

img = cv2.imread("assets/sample.jpg")

# Bilateral blur
##@ smoothing.py
# * most effective
img_bilateral = cv2.bilateralFilter(
    # the image
    img,
    # diameter
    # * more diameter, more blur
    15,
    # color sigma
    # * how much color is considered
    # * more colors are considered
    10,
    # space sigma
    # * distance in pixels that will affect the result
    105,
)

# ! Remove green channel
# > didn't work as expected, so I left here
# > as a reference
#
# remove_green_channel_from = img_bilateral
# zeros = np.zeros(remove_green_channel_from.shape[:2], dtype=np.uint8)
# g,b,r = cv2.split(remove_green_channel_from)
# img_no_green = cv2.merge((b, zeros, r))

# HSV
img_hsv = cv2.cvtColor(img_bilateral, cv2.COLOR_BGR2HSV)

cv2.imshow("Image", img)
# cv2.imshow("No green", img_no_green)
# cv2.imshow("Bilateral Blur", img_bilateral)
cv2.imshow("HSV", img_hsv / img_bilateral)

cv2.waitKey(0)
