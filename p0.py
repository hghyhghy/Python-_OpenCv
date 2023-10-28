
import cv2

import numpy as np

import matplotlib.pyplot as plt

# reading the image using cv2

img=cv2.imread("dar.jpg")

# isplaying the image  using plt

plt.imshow(img)

# hold the window until the button pressed 
plt.waitforbuttonpress()

plt.close(all)