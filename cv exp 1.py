import cv2
image= cv2.imread("C:/Users/ADMIN/Desktop/tree.jpg")
cv2.imshow('original',image)
cv2.waitKey(0)
gray_image= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow('Grayimage',gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
