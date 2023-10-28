
#  showing the image byusing path 

import cv2

path=r"C:\Users\subha\Desktop\OpenCV\dar.jpg"

# image reading 

img=cv2.imread(path)

# naming the window 

wwindow_name="Images"

cv2.imshow(wwindow_name,img)

# wating the window 

cv2.waitKey(0)

