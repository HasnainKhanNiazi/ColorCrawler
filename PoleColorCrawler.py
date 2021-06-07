import cv2
import numpy as np
import cv2

image = cv2.imread('Updated.jpg', 1)
image = cv2.resize(image,(800,800))
x = 396
y = 104
w = 29
h = 364

Just_Pole = image[y:y+h,x:x+w]

counter = 1

Green_Min = [[]]
Green_Max = [[]]
Red_Min = [[]]
Red_Max = [[]]
Blue_Min = [[]]
Blue_Max = [[]]

G_min = 0
G_max = 0
R_min = 0
R_max = 0
B_min = 0
B_max = 0

CC = True

for first_row in range(0,len(Just_Pole)):
    for j in range(0, len(Just_Pole[first_row])):
        if CC == True:
            # Assign min and max at the start of each main row as there are sub-rows also
            R_min = Just_Pole[first_row][j][0]
            R_max = Just_Pole[first_row][j][0]
            G_max = Just_Pole[first_row][j][1]
            G_min = Just_Pole[first_row][j][1]
            B_max = Just_Pole[first_row][j][2]
            B_min = Just_Pole[first_row][j][2]
        if Just_Pole[first_row][j][0] < R_min:
            R_min = Just_Pole[first_row][j][0]
        elif Just_Pole[first_row][j][0] > R_max:
            R_max = Just_Pole[first_row][j][0]
        elif Just_Pole[first_row][j][1] < G_min:
            G_min = Just_Pole[first_row][j][1]
        elif Just_Pole[first_row][j][1] > G_max:
            G_max = Just_Pole[first_row][j][1]
        elif Just_Pole[first_row][j][2] < B_min:
            B_min = Just_Pole[first_row][j][2]
        elif Just_Pole[first_row][j][2] > B_max:
            B_max = Just_Pole[first_row][j][2]
        else:
            print("Value Would be Equal Then")
        CC = False
    CC = True
    Red_Max.append([counter,R_max])
    Red_Min.append([counter,R_min])
    Green_Max.append([counter,G_max])
    Green_Min.append([counter,G_min])
    Blue_Max.append([counter,B_max])
    Blue_Min.append([counter,B_min])
    counter += 1
        
with open('RGB_Ranges.txt', 'w') as filehandle:
    filehandle.write("Sequence is RGB")
    for i in range(1, len(Red_Max)):
        filehandle.write("\n ************ Row Number " + str(i) + "************")
        filehandle.write("\n Min is: " + str(Red_Min[i][1]) + "," + str(Green_Min[i][1]) + "," + str(Blue_Min[i][1]) + " ** " + "Max is: " + str(Red_Max[i][1]) + "," + str(Green_Max[i][1]) + "," + str(Blue_Max[i][1]))