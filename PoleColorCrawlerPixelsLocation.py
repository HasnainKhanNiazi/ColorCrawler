import cv2
import numpy as np
import pandas as pd
import os

def main():
    image = cv2.imread('Updated.jpg', 1)
    image = cv2.resize(image,(800,800))
    x = 396
    y = 104
    w = 29
    h = 364

    # rgb(165,42,42) --> Brown
    # X = 396 + 29 --> 425
    # Y = 104 + 364 --> 468 
    # location = []
    # for xL in range(396,425):
    #     for yL in range(104, 468):
    #         location.append((xL,yL))
    newLocation = []
    for newX in range(396,425):
        for newY in range(104, 735):
            newLocation.append((newY, newX))

    print(newLocation[-1])
    # for jj in range(len(newLocation)):
    #     print(newLocation[jj])

    #     if jj == 100:
    #         break

    # Just_Pole = image[y:y+h,x:x+w]

    for l in range(0,len(newLocation)):
        image[newLocation[l]] = [42,42,165]
    cv2.imshow("New Images",image)
    # cv2.imwrite("newUpdated.jpg",image)
    cv2.waitKey(0)

if __name__=="__main__":
    main()