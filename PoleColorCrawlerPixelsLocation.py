import cv2
import numpy as np
import pandas as pd
import os
from PIL import *
from PIL import Image

def main():
    image = cv2.imread('Updated.jpg', 1)
    image = cv2.resize(image,(800,800))

    imagee = Image.open("Updated.jpg")
    f = imagee.load()

    x = 396
    y = 104
    w = 29
    h = 364
    points = bbox_dict_to_list(x,y,w,h,(800,800))
    print(points)
    # Just_Pole = image[y:y+h,x:x+w]

def bbox_dict_to_list(l,t,w,h, image_size):
#   h = bbox_dict.get('height')
#   l = bbox_dict.get('left')
#   t = bbox_dict.get('top')
#   w = bbox_dict.get('width')

  img_w, img_h = image_size

  x1 = l/img_w
  y1 = t/img_h
  x2 = (l+w)/img_w
  y2 = (t+h)/img_h
  return [x1, y1, x2, y2]

if __name__=="__main__":
    main()