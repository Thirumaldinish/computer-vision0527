
import cv2
image = cv2.imread("C:/Users/ADMIN/Desktop/tree.jpg")
cv2.imshow('original',image)
cv2.waitKey(0)
height, width = image.shape[:2]
flipped_image = cv2.flip(image, 1)
rotated_image = cv2.transpose(flipped_image)
cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('rotated_image.jpg', rotated_image)
