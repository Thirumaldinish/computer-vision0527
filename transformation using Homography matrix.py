import cv2
import numpy as np
im_src = cv2.imread(r"C:\Users\ADMIN\Pictures\images (1).jfif")
im_dst = cv2.imread(r"C:\Users\ADMIN\Downloads\images.jfif")
if im_src is None:
    print("Error: Source image not loaded correctly.")
    exit()

if im_dst is None:
    print("Error: Destination image not loaded correctly.")
    exit()
pts_src = np.array([[141, 131], [480, 159], [493, 630], [64, 601]])
pts_dst = np.array([[318, 256], [534, 372], [316, 670], [73, 473]])
h, status = cv2.findHomography(pts_src, pts_dst)
im_out = cv2.warpPerspective(im_src, h, (im_dst.shape[1], im_dst.shape[0]))
small_im_dst = cv2.resize(im_dst, (im_dst.shape[1] // 4, im_dst.shape[0] // 4))
cv2.imshow("Source Image", im_src)
cv2.imshow("Destination Image", small_im_dst)
cv2.imshow("Warped Source Image", im_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
