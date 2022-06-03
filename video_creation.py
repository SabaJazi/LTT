import numbers
from tokenize import Number
import cv2
import os

image_folder = 'd:/LTT/frames'
video_name = 'original.avi'
#what is the type of os.listdr??
images = [img for img in sorted(os.listdir(image_folder)) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 7, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()