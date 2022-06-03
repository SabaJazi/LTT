import os
from PIL import Image, ImageDraw
import os
import cv2
import numpy as np

# test 1 sample
image_folder = 'd:/LTT/frames/1.jpg'

img=cv2.imread(os.path.join(image_folder))
h, w, layers = img.shape
# image blending formula in openCV:
# https://medium.com/featurepreneur/blending-images-using-opencv-bfc9ab3697b7
# g(x) = alpha . src1 + beta . src2
# beta = 1 - alpha

# First we crop the sub-rect from the image
x, y, w, h = 130, 350, 200, 15
# src 1
sub_img = img[y:y+h, x:x+w]
# src 2
black_rect = np.zeros(sub_img.shape, dtype=np.uint8) * 255

# alpha=0.6 , beta=0.4 , gamma=1.0
res = cv2.addWeighted(sub_img, 0.9, black_rect, 0.1, 1.0)

# Putting the image back to its position
img[y:y+h, x:x+w] = res
filename = 'occl_0.9.jpg'
cv2.imwrite(filename, img)

# Create copy and make bottom part black
# dark = frame.copy()
# draw  = ImageDraw.Draw(dark)
# draw.rectangle((0, int(0.7*h), w, h), 0)
# dark.save('dark.png') 

# # Blend darkened copy over top of background
# blended = Image.blend(frame, dark, 0.7) 
# blended.save('blended2.png')   