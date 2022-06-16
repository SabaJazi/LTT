import os
# from PIL import Image, ImageDraw
import os
import cv2
import numpy as np

image_folder = 'd:/LTT/frames'
save_path='d:/LTT/fixed_frames'

imgs=[]
images = [img for img in os.listdir(image_folder)  if 
            img.endswith(".jpg")]

for img in images:
    img=img[:-4]
    imgs.append(int(img))
imgs=sorted(imgs)

np_img=np.array(imgs)

fixed_num=np_img -1
# print(fixed_num)
for img in np_img:
    image=cv2.imread(os.path.join(image_folder, str(img)+'.jpg'))
    cv2.imwrite(os.path.join(save_path , str(img-1)+".jpg"), image)
    