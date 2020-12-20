#by 俊榮
import os
import glob
import shutil
import cv2
from skimage import io

source_dir_jpeg = "/home/JPEGImages/"

# change to the source directory
os.chdir(source_dir_jpeg)

# sort the file alphabetically
list_dir = os.listdir(source_dir_jpeg)
list_dir = [file for file in list_dir]
list_dir= sorted(list_dir)

def verify_image(img_file):
  try:
       img = io.imread(img_file)
  except:
	return False
  return True

for i, img in enumerate(list_dir):
  pct = i/(len(list_dir))
  #print(str(round(pct, 2)*100) + "% completed...")
  #bgr=cv2.imread(source_dir_jpeg+img)
  if not verify_image(source_dir_jpeg+img):
     #print("passed!")
     print(source_dir_jpeg+img)


print("complete 100%")

