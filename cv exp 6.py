
import cv2
image = cv2.imread("C:/Users/ADMIN/Desktop/tree.jpg")
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()