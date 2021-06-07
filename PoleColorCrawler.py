import cv2
import numpy as np
import tqdm
import os

# Actual
# lower_green = np.array([25, 52, 72])
# upper_green = np.array([102, 255, 255])


# filename = "C:/Users/HP/Desktop/0a5ed2b8-a13d-467b-9f44-52842a5c77a5.jpg"

# imga=cv2.imread(filename)
# hsv = cv2.cvtColor(imga, cv2.COLOR_BGR2HSV)
# greenmask = cv2.inRange(hsv, lower_green, upper_green)
# rows = greenmask.shape[0]
# cols = greenmask.shape[1]
# image = np.zeros((rows, cols, 3), dtype=np.uint8)
# image[np.where(greenmask == 0)] = (0, 0, 0)
# image[np.where(greenmask != 0)] = (0, 128, 0)
# # cv2.imwrite("./{}".format(os.path.basename(filename)), imga)
# cv2.imwrite("./{}_mask.png".format(os.path.basename(filename)), image)


"""
# NEW
import cv2

class BoundingBoxWidget(object):
    def __init__(self):
        self.original_image = cv2.imread('Updated.jpg')
        self.original_image = cv2.resize(self.original_image,(800,800))
        self.clone = self.original_image.copy()

        cv2.namedWindow('image')
        cv2.setMouseCallback('image', self.extract_coordinates)

        # Bounding box reference points
        self.image_coordinates = []

    def extract_coordinates(self, event, x, y, flags, parameters):
        # Record starting (x,y) coordinates on left mouse button click
        if event == cv2.EVENT_LBUTTONDOWN:
            self.image_coordinates = [(x,y)]

        # Record ending (x,y) coordintes on left mouse button release
        elif event == cv2.EVENT_LBUTTONUP:
            self.image_coordinates.append((x,y))
            print('top left: {}, bottom right: {}'.format(self.image_coordinates[0], self.image_coordinates[1]))
            print('x,y,w,h : ({}, {}, {}, {})'.format(self.image_coordinates[0][0], self.image_coordinates[0][1], self.image_coordinates[1][0] - self.image_coordinates[0][0], self.image_coordinates[1][1] - self.image_coordinates[0][1]))

            # Draw rectangle 
            cv2.rectangle(self.clone, self.image_coordinates[0], self.image_coordinates[1], (36,255,12), 2)
            cv2.imshow("image", self.clone) 

        # Clear drawing boxes on right mouse button click
        elif event == cv2.EVENT_RBUTTONDOWN:
            self.clone = self.original_image.copy()

    def show_image(self):
        return self.clone

if __name__ == '__main__':
    boundingbox_widget = BoundingBoxWidget()
    while True:
        cv2.imshow('image', boundingbox_widget.show_image())
        key = cv2.waitKey(1)

        # Close program with keyboard 'q'
        if key == ord('q'):
            cv2.destroyAllWindows()
            exit(1)

"""

import cv2
image = cv2.imread('Updated.jpg', 1)
image = cv2.resize(image,(800,800))
x = 396
y = 104
w = 29
h = 364

Just_Pole = image[y:y+h,x:x+w]

# Convert image to NumPy array
img_array = np.array(Just_Pole, dtype=np.uint8)
# ... do some operation on NumPy array (copy rows to lists, etc.) ...

# print(len(img_array))

first = img_array[0]
smallest = first.min()
largest = first.max()
print(first)

# cv2.imshow("Cutted Image",Just_Pole)
# cv2.waitKey(0)