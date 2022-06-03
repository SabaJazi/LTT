import numbers
from tokenize import Number
import cv2
import os
import numpy as np

# frames directory for input
image_folder = 'd:/LTT/frames'

# output directory to save the video
video_name = 'original_7fps.avi'

imgs=[]
images = [img for img in os.listdir(image_folder)  if img.endswith(".jpg")]
# removing the .jpg and adding the int of images names to list
# if we read the images names the 10 will come after 1 instead of 2 after 1
for img in images:
    img=img[:-4]
    imgs.append(int(img))

imgs=sorted(imgs)
np_img=np.array(imgs)
# getting the shape of frames by reading one frame
frame=cv2.imread(os.path.join(image_folder, str(np_img[0])+'.jpg'))
height, width, layers = frame.shape
# setting the frame rate (here it is 7) and video name and sizes
video = cv2.VideoWriter(video_name, 0, 7, (width,height))

for image in np_img:
    video.write(cv2.imread(os.path.join(image_folder, str(image)+'.jpg')))
cv2.destroyAllWindows()
video.release()