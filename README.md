# Miscellaneous
<<<<<<< HEAD
<<<<<<< HEAD
Miscellaneous tools and scripts for data preprocessing and machine learning. The scripts implemented here are just for personal use, where these scripts are just for my convenience for cases that I have come across, but feel free to use them if needed.

### Python Scripts (`.py`)
* `crop.py` - Can be used to generate more dataset by cropping images that are already labelled. Assuming that there are image labels using [LabelImg](https://github.com/tzutalin/labelImg) (i.e., each JPG image contains its own XML label), images will be cropped based on the ratio set, while generating a corresponding XML label of the same name, which has a corresponding bounding box based on the crop ratio. Take in arguments in console using ArgParse. 
* `daynight.py` - Separate images by day and night and renaming them via hours on timestamp. Needs the usage of `ComparisonSet.zip` files to compare the time in the timestamp. Comparison is done by pixel on the values at the top right of the image (which shows the timestamp hour).
* `diffchecker.py` - Check anomalies between JPG and XML file for unlabelled files. Reads data from path in `config.txt` file, or can be set in the Python file.
* `groundtruth.py` - Get path and final labels of file name and write them to a text file. Usually used in getting ground truth (actual labels).
* `iou.py` - Calculate Intersection-over-Union (IoU) for labeled images, ground truth and prediction. The process is done by generating two text files, `GT.txt` and `Predict.txt`, then making the IoU comparison. To run the script again, previously generated `GT.txt` and `Predict.txt` files have to be deleted beforehand to avoid conflicts. Path is configured/obtained from `config.txt`.
* `labelchecker.py` - Assume that images are labelled using [LabelImg](https://github.com/tzutalin/labelImg), this script checks for image which labels are out of bounds/cropped wrongly/not detected, and move XML label files to xml folder.
* `multiple.py` - Read files from a parent directory and also files in child sub-directories.
* `otsu.py` - Convert images to Otsu and histogram equalized using OpenCV. Then, both operations are combined using bitwise AND.
* `rename.py` - Rename batch files for JPG and XML file of the same name into incrementing sequence. Reads data from path in `config.ini` file.
* `resize.py` - Assuming that images are labelled using [LabelImg](https://github.com/tzutalin/labelImg), batch of images are resized from 1080p to 720p, then placed in a configured save path. The bounding boxes for each XML label file are also resized accordingly.
* `teststream.py` - Streaming video with RTSP.
* `writer.py` - Write a text file separated by each line on a list. 
* `writexml.py` - Write an empty XML label containing boundaries for an image file, suitable to generate empty labels for images to be labelled accordingly (i.e., using LabelImg to label the images manually after that).

### Python Notebooks (`.ipynb`)
* `BeautifulSoup.ipynb` - Web scraping from XML in website using Beautiful Soup. Still incomplete.
* `imgaug_mix.ipynb` - Script to generate augmented datasets using [Aleju's ImgAug Library](https://github.com/aleju/imgaug).

### JavaScript 
* `hackerman.js` - Script to auto reconnect for Google Colab, reconnect interval is set in milliseconds. Has to be run in browser JavaScript console.

### C/C++
* `post.cpp` - HTTP Post with CPP using cURL library. Example taken from [this website](https://qiita.com/ekzemplaro/items/97bc000576a6210a3068).

### Others
* `Comparison.zip` - Image files, used with `daynight.py`.
* `config.ini` - Config file. Used with `rename.py`.
* `config.txt` - Config file. Used with `diffchecker.py`, `iou.py`.
* `logs.sh` - Shell script to extract docker logs to docker_logs folder with subfolder of current date and time. You may check out my implementation of automatically installing and configuring Docker containers on my Git [here](https://github.com/tiongsikng/docker).
=======
=======
Miscellaneous tools and scripts for data preprocessing and machine learning.
>>>>>>> fd76edf... Update README.md

### Python Scripts (`.py`)
* `crop.py` - Cropping images with labels, where JPG and XML files have the same name. The labels will be generated in new XML files accordingly after cropping and generating the new images.
* `daynight.py` - Separate images by day and night and renaming them via hours on timestamp. Needs the usage of ComparisonSet.zip files to compare the time in the timestamp.
* `diffchecker.py` - Check anomalies between JPG and XML file. Reads data from path in config.txt file.
* `groundtruth.py` - Get path and final labels of file name and write them to a text file.
* `iou.py - Calculate Intersection-over-Union (IoU) for labeled images, ground truth and prediction. Previously generated GT.txt and Predict.txt files have to be deleted beforehand to avoid conflicts.
* `labelchecker.py` - Check for image which labels are out of bounds/cropped wrongly/not detected, and move XML label files to xml folder.
* `multiple.py` - Read files from a parent directory and also files in child sub-directories.
* `otsu.py` - Convert images to otsu and histogram equalize. Also combines both operations using bitwise AND.
* `rename.py` - Rename batch files for JPG and XML file of the same name, incrementing. Reads data from path in config.ini file.
* `resize.py` - Resize batch of images from 1080p to 720p. Also resize the bounding boxes for each XML label file.
* `teststream.py` - Streaming video with RTSP.
* `writer.py` - Write a text file separated by each line on a list. 
* `writexml.py` - Write an empty XML label containing boundaries for an image file.

### Python Notebooks (`.ipynb`)
* `BeautifulSoup.ipynb` - Web scraping from XML in website using Beautiful Soup. Still incomplete.
* `imgaug_mix.ipynb` - Script to generate augmented dataset.

### JavaScript 
* `hackerman.js` - Script to auto reconnect for Google Colab, reconnect interval is set in milliseconds.

### C/C++
* `post.cpp` - HTTP Post with CPP using cURL library. Example taken from [this website](https://qiita.com/ekzemplaro/items/97bc000576a6210a3068).

### Others
<<<<<<< HEAD
* logs.sh - Shell script to extract docker logs to docker_logs folder with subfolder of current date and time.
>>>>>>> 5592f8e... Initial commit
=======
* `logs.sh` - Shell script to extract docker logs to docker_logs folder with subfolder of current date and time.
>>>>>>> fd76edf... Update README.md
