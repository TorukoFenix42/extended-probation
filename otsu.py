import os, glob
import numpy as np
import cv2

<<<<<<< HEAD
path = '/home/dataset/'
newpath = '/home/new_dataset/'
=======
path = '/media/imageDB/LPR/0_NewData/vlp-022-my-r/VLP_dataset/'
newpath = '/media/imageDB/LPR/LPR_trainset/Hist_Otsu/vlp-022-my-r/VLP_dataset/'
>>>>>>> 5592f8e... Initial commit
count = 0

for files in sorted(glob.glob(os.path.join(path, "*.jpg"))):
    img = cv2.imread(files)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # mask for bitwise AND
    ret, mask = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # equalize histogram
    eqhist = cv2.equalizeHist(img)
    print("Eq Histogram ", eqhist.shape)

    # otsu threshold
    ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    print("Threshold ", thresh.shape)

    # bitwise AND for otsu and histogram
    newthresh = np.add(eqhist, thresh)
    img = cv2.bitwise_and(eqhist, thresh, mask=newthresh)

    img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
    img_H, img_W, img_C = img.shape

    new_name = os.path.basename(files)
    filename = os.path.join(newpath, new_name)
    cv2.imwrite(filename, img)
    print(files, '>>', filename)
    count += 1