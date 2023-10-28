

# converting the BGR image to RGB 

import cv2

import numpy as np

import matplotlib.pyplot as plt

# reading the image 

img=cv2.imread("dar.jpg")

# converting bgr to rgb 

RGB_img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# showing  the images 

plt.imshow(RGB_img)

# holding the window 

plt.waitforbuttonpress()

plt.close(all)
