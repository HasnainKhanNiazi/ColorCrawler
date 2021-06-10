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
    h = 631

    # rgb(165,42,42) --> Brown
    # X = 396 + 29 --> 425
    # Y = 104 + 364 --> 468 
    location = []
    for xL in range(396,(396+29)):
        for yL in range(104, (104+631)):
            location.append((yL,xL))

    Just_Pole = image[y:y+h,x:x+w]

    for l in range(0,len(location)):
        image[location[l]] = [42,42,165]
    
    cv2.imshow("New Images",image)
    cv2.imwrite("newUpdated.jpg",image)
    cv2.waitKey(0)
    print(len(Just_Pole))
    locationCounter = 0
    with open('RGB_Ranges.txt', 'w') as filehandle:
        filehandle.write("Sequence is RGB")
        for mm in range(len(Just_Pole)):
            filehandle.write("\n ************ Row Number " + str(mm) + "************")
            for nn in range(len(Just_Pole[mm])):
                filehandle.write("\n RGB value is : " + str(Just_Pole[mm][nn][0]) + "," + str(Just_Pole[mm][nn][0]) + "," + str(Just_Pole[mm][nn][0]) + " ** " + "At X,Y Location " + str(location[locationCounter]))
                locationCounter += 1




if __name__=="__main__":
    main()