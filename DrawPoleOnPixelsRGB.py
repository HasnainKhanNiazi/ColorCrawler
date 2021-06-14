import numpy as np
import cv2
import math
from math import pow
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000

THRESHOLD = 18

def ColorDistance(rgb1,rgb2):
    '''d = {} distance between two colors(3)'''
    rm = 0.5*(rgb1[0]+rgb2[0])
    d = sum((2+rm,4,3-rm)*(rgb1-rgb2)**2)**0.5
    return d

def luminance(pixel):
    return (0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])


def is_similar(pixel_a, pixel_b, threshold):
    return abs(luminance(pixel_a) - luminance(pixel_b)) < threshold



def ColorDifferenceUsingEuclideanDistance(Color1, Color2):
    x = Color1[0] - Color2[0]
    y = Color1[1] - Color2[1]
    z = Color1[2] - Color2[2]
    d = int(pow(x,2)) + int(pow(y,2)) + int(pow(z,2)) # Actual Distance
    p = d /math.sqrt((255)^2+(255)^2+(255)^2) # Percentage
    return p

def ColorMathFn(Color1,Color2):
    # Red Color
    color1_rgb = sRGBColor(Color1[0], Color1[1], Color1[2])

    # Blue Color
    color2_rgb = sRGBColor(Color2[0], Color2[1], Color2[2])

    # Convert from RGB to Lab Color Space
    color1_lab = convert_color(color1_rgb, LabColor)

    # Convert from RGB to Lab Color Space
    color2_lab = convert_color(color2_rgb, LabColor)

    # Find the color difference
    delta_e = delta_e_cie2000(color1_lab, color2_lab)

    return delta_e
    # print ("The difference between the 2 color = ", delta_e)


def main():
    image = cv2.imread("newOne.jpg", 1)
    # image = cv2.cvtColor(image,cv2.COLOR_RGB2HSV)
    x,y = 420,69
    # Color1 = image[420][69]
    Color1 = [158,136,121]
    # Color2

    # print(image.shape)
    print(image[420][69])
    for xx in range(420,len(image)):
        for yy in range(69,len(image[xx])-1):
            # Color1 = image[xx][yy]
            Color2 = image[xx][yy + 1]
            # d = ColorDistance(Color1, Color2)
            d = is_similar(Color1, Color2, THRESHOLD)
            # d = ColorMathFn(Color1, Color2)
            # d = ColorDifferenceUsingEuclideanDistance(Color1,Color2)
            if d < 1:
                image[yy,xx] = [255,255,255]
                # print(d)
                # continue
            else:
                # print(d)
                continue
                # image[yy,xx] = [255,255,255]
                # print("here 1")


    cv2.imshow("Image",image)
    cv2.imwrite("ResultWithLuuminace.jpg",image)
    cv2.waitKey(0)

if __name__=="__main__":
    main()

