import cv2
import numpy as np


x_start = 429 - 20
x_end = 3609 + 50
y_start = 1619 - 50
y_end = 1695 + 20

print(x_start)
def main():
    image = cv2.imread("1e23c283-7047-4377-ad8a-46d60ec54033.jpg", 1)
    for xx in range(x_start,x_end):
        for yy in range(y_start,y_end):
            image[xx,yy] = [255,255,255]

    cv2.imshow("Image",image)
    cv2.imwrite("ResultWithPixels.jpg",image)
    cv2.waitKey(0)


if __name__=="__main__":
    main()