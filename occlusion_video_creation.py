import os
# from PIL import Image, ImageDraw
import os
import cv2
import numpy as np

# # test 1 sample
# image_folder = 'd:/LTT/frames/1.jpg'

# img=cv2.imread(os.path.join(image_folder))
# # h, w, layers = img.shape
# # image blending formula in openCV:
# # https://medium.com/featurepreneur/blending-images-using-opencv-bfc9ab3697b7
# # g(x) = alpha . src1 + beta . src2
# # beta = 1 - alpha

# # First we crop the sub-rect from the image
# x, y, w, h = 130, 350, 200, 15
# # src 1
# sub_img = img[y:y+h, x:x+w]
# # src 2
# # we make a black copy of cropped part
# black_rect = np.zeros(sub_img.shape, dtype=np.uint8) * 255

# # blend with the original part
# # alpha=0.6 , beta=0.4 , gamma=1.0
# res = cv2.addWeighted(sub_img, 0.9, black_rect, 0.1, 1.0)

# # Putting the blended part back to its position
# img[y:y+h, x:x+w] = res
# # saving the new image
# filename = 'occl_0.9.jpg'
# cv2.imwrite(filename, img)
# -----------------------------------------------------------------------------

image_folder = 'd:/LTT/frames'
video_name = 'd:/LTT/occl_videos/occl_middle_09.avi'
# save_path='d:/LTT/occl_top_09_frames'
# save_path='d:/LTT/occl_top_075_frames'
# save_path='d:/LTT/occl_middle_075_frames'
save_path='d:/LTT/occl_middle_09_frames'

imgs=[]
images = [img for img in os.listdir(image_folder)  if img.endswith(".jpg")]
# removing the .jpg and adding the int of images names to list
# if we read the images names the 10 will come after 1 instead of 2 after 1
for img in images:
    img=img[:-4]
    imgs.append(int(img))
imgs=sorted(imgs)
np_img=np.array(imgs)

frame=cv2.imread(os.path.join(image_folder, str(np_img[0])+'.jpg'))
height, width, layers = frame.shape
video = cv2.VideoWriter(video_name, 0, 7, (width,height))
x, y, w, h = 130, 380, 200, 15

for img in np_img:
    image=cv2.imread(os.path.join(image_folder, str(img)+'.jpg'))
    if img>24:
        sub_img = image[y:y+h, x:x+w]
        black_rect = np.zeros(sub_img.shape, dtype=np.uint8) * 255
        res = cv2.addWeighted(sub_img, 0.9, black_rect, 0.1, 1.0)
        image[y:y+h, x:x+w] = res
    cv2.imwrite(os.path.join(save_path , str(img)+".jpg"), image)
    video.write(image)
cv2.destroyAllWindows()
video.release()