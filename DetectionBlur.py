import cv2
original = cv2.imread("Detection.jpg", 3)
blurred = cv2.GaussianBlur(original, (25,25), 0)

original[0:500, 0:500] = blurred[0:500, 0:500]

#1358.99560546875, 293.4925231933594, 152.9748992919922, 261.75750732421875, 23.010772705078125

cv2.imwrite('cvBlurredOutput.jpg', original)