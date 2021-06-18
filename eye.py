#-*- coding:utf-8 -*-
import cv2
def solve(img):
    rows,cols,_=img.shape
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img_gas=cv2.GaussianBlur(img_gray,(7,7),0)
    img_threshold = cv2.threshold(img_gas, 0, 255, cv2.THRESH_OTSU+cv2.THRESH_BINARY_INV)[1]
    cv2.imshow("huidu",img_threshold)
    contours, _ = cv2.findContours(img_threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
    # print(contours)
    for cnt in contours:
        (x, y, w, h) = cv2.boundingRect(cnt)
        # cv2.drawContours(roi, [cnt], -1, (0, 0, 255), 3)
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 1)
        cv2.line(img, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 1)
        cv2.line(img, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 1)
        # print("jinqule")
        break
    # cv2.imshow("roi",img)
    # return img