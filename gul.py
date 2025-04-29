import cv2
import numpy as np

def apply_color_change(img, mask, diff_hue, bright_change): 
    image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(image) 
    hnew = np.mod(h + diff_hue, 180).astype(np.uint8) 
    vnew = np.clip(v + bright_change, 0, 255).astype(np.uint8) 
    hsv_new = cv2.merge([hnew, s, vnew]) 
    bgr_new = cv2.cvtColor(hsv_new, cv2.COLOR_HSV2BGR) 
    mask_3ch = cv2.merge([mask, mask, mask]) 
    result = np.where(mask_3ch == 255, bgr_new, 0)  
    return result


img = cv2.imread("input.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lower_red = np.array([111, 22, 0])
upper_red = np.array([180, 255, 255])


mask = cv2.inRange(hsv, lower_red, upper_red)


kernel_open = np.ones((17, 17), np.uint8)
kernel_close = np.ones((7, 7), np.uint8)
iterasyon = 2

closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel_close, iterasyon)

opening = cv2.morphologyEx(closing , cv2.MORPH_OPEN, kernel_open, iterasyon)


diff_hue = 220
brightness_change = 0

mor_gul = apply_color_change(img, opening, diff_hue= diff_hue, bright_change= brightness_change)

gul = cv2.bitwise_and(img, img, mask= opening)


cv2.imshow("orginal", img)
cv2.imshow("mask imrange", mask)
cv2.imshow("clossing", closing)
cv2.imshow("opening", opening)
cv2.imshow("orginal gul", gul)
cv2.imshow("mor gul", mor_gul)

cv2.imwrite("output.jpg", mor_gul)


cv2.waitKey(0)
cv2.destroyAllWindows()


