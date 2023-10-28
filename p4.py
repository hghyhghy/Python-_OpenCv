

# the imwrite() method 

import cv2

import os

Path=r"C:\\Users\\subha\\Desktop\\OpenCV\\dar.jpg"

#  current directory

directory=r"C:\\Users\\subha\\Desktop\\OpenCV>"

# reading the image 

img=cv2.imread(Path)

# change the current directory

os.chdir(directory)

print("Before changing the image  ")

print(os.listdir(directory))

filename="Darjeeling.jpg"

cv2.imwrite(filename,img)

print("Before changing the image  ")

print(os.listdir(directory))

print("Saved successfully")
