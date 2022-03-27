##@ next: fun-lol.py
##@ prev: hsv.py

import cv2

img = cv2.imread("assets/sample.jpg")

# Averaging
average = cv2.blur(img, (7, 7))

# Gaussian
# sigmaX is standard deviation in X direction
gaussian = cv2.GaussianBlur(img, (7, 7), 0)

# Median
# * good to remove noise
median = cv2.medianBlur(img, 9)

# Bilateral
# * most effective
bilateral = cv2.bilateralFilter(
    img,
    # diameter
    # * more diameter, more blur
    15,
    # color sigma
    # * how much color is considered
    # * more colors are considered
    85,
    # space sigma
    # * distance in pixels that will affect the result
    75,
)

cv2.imshow("Image", img)
# cv2.imshow("Average Blur", average)
# cv2.imshow("Gaussian Blur", gaussian)
# cv2.imshow("Median Blur", median)
cv2.imshow("Bilateral Blur", bilateral)

cv2.waitKey(0)
