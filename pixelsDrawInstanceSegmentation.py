import cv2
import numpy as np
import csv

x_start = 429
x_end = 3609 + 20
y_start = 1619
y_end = 1695 + 20

print(x_start)
def main():
    image = cv2.imread("1e23c283-7047-4377-ad8a-46d60ec54033.jpg", 1)
    with open('innovators.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["X", "Y", "RGB", "InsidePole"])
        for xx in range(x_start,x_end):
            for yy in range(y_start,y_end):
                if xx <= 3609 and yy <=1695:
                    writer.writerow([xx, yy, image[xx,yy], "True"])
                else:
                    writer.writerow([xx, yy, image[xx,yy], "False"])
                # image[xx,yy] = [255,255,255]

    # cv2.imshow("Image",image)
    # cv2.imwrite("ResultWithPixels.jpg",image)
    # cv2.waitKey(0)


if __name__=="__main__":
    main()