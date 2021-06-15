import cv2
import numpy as np
import tqdm
import os

lower_brown = np.array([50, 50, 20]) # a dark brown
upper_brown = np.array([138, 187, 194]) # BGR of your brown

# lower_green = np.array([103,96,91])
# upper_green = np.array([32,26,23])

filename = "C:/Users/HP/Desktop/0a5ed2b8-a13d-467b-9f44-52842a5c77a5.jpg"

imga=cv2.imread(filename)
hsv = cv2.cvtColor(imga, cv2.COLOR_BGR2HSV)
greenmask = cv2.inRange(hsv, lower_brown, upper_brown)
rows = greenmask.shape[0]
cols = greenmask.shape[1]
image = np.zeros((rows, cols, 3), dtype=np.uint8)
image[np.where(greenmask == 0)] = (0, 0, 0)
image[np.where(greenmask != 0)] = (0, 128, 0)
# cv2.imwrite("./{}".format(os.path.basename(filename)), imga)
cv2.imwrite("./{}_mask.png".format(os.path.basename(filename)), image)

