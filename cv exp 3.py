import cv2
import numpy as np
image = cv2.imread("C:/Users/ADMIN/Desktop/tree.jpg")
cv2.imshow('Original Image', image)
cv2.waitKey(0)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, 100, 200)
cv2.imshow('Canny Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
