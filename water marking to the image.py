import cv2
img = cv2.imread(r"C:\Users\ADMIN\Pictures\images (1).jfif")
wm = cv2.imread(r"C:\Users\ADMIN\Downloads\images.jfif")
h_wm, w_wm = wm.shape[:2]
h_img, w_img = img.shape[:2]
center_x = int(w_img / 2)
center_y = int(h_img / 2)
top_y = center_y - int(h_wm / 2)
left_x = center_x - int(w_wm / 2)
bottom_y = top_y + h_wm
right_x = left_x + w_wm
if w_wm > w_img or h_wm > h_img:
    wm = cv2.resize(wm, (right_x - left_x, bottom_y - top_y))
if wm.shape[2] == 1:
    wm = cv2.cvtColor(wm, cv2.COLOR_GRAY2BGR)
roi = img[top_y:bottom_y, left_x:right_x]
if wm.shape[:2] != roi.shape[:2]:
    wm = cv2.resize(wm, (roi.shape[1], roi.shape[0]))
result = cv2.addWeighted(roi, 1, wm, 0.3, 0)
img[top_y:bottom_y, left_x:right_x] = result
cv2.imshow("Watermarked Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
