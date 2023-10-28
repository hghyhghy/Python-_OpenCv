
#  showing the image byusing path 

import cv2

path=r"C:\Users\subha\Desktop\OpenCV\dar.jpg"

# image reading  in grayscale mode

img=cv2.imread(path,0)

# naming the window 

wwindow_name="Images"

cv2.imshow(wwindow_name,img)

# wating the window 

cv2.waitKey(0)

