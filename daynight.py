from PIL import Image
import glob
import numpy as np
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import os


def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])


def normalise(x):
    mini = np.min(x);
    maxi = np.max(x)
    return (x - mini) / (maxi - mini)

def createfolder(whatever):
    try:
        os.makedirs(whatever)
    except OSError:
        pass


<<<<<<< HEAD
<<<<<<< HEAD
path = '/home/GT_DayNight/'
comparisonpath = '/home/' + 'ComparisonSet/*.jpg'
=======
path = '/media/imageDB/LPR/5_testset/WCE/lpd/wce_0803/GT_DayNight/'
comparisonpath = '/media/imageDB/LPR/5_testset/WCE/lpd/wce_0803/' + 'ComparisonSet/*.jpg'
>>>>>>> 5592f8e... Initial commit
=======
path = '/home/GT_DayNight/'
comparisonpath = '/home/' + 'ComparisonSet/*.jpg'
>>>>>>> 34fe968... Update some configs and README
testingpath = path + '*.jpg'
labelset = glob.glob(comparisonpath)
testset = glob.glob(testingpath)

x1 = 1705
x2 = 1751
y1 = 16
y2 = 49

threshold = 1
comparisonpixel = [];
checking = False

for f in labelset:
    img = mpimg.imread(f)
    gray = normalise(rgb2gray(img))[y1:y2, x1:x2]
    gray[gray >= threshold] = 1
    comparisonpixel.append(gray)

for f in testset:
    img = mpimg.imread(f)
    gray = normalise(rgb2gray(img)[y1:y2, x1:x2])
    gray[gray >= threshold] = 1
    distance = []

    for i in range(len(labelset)):
        distance.append(np.square(comparisonpixel[i] - gray).sum())
    index = np.argmin(distance)
    print(f, ' is : ', index)
    if index >= 6 and index <= 19:
        os.rename(f, f[:-4] + '_D.jpg')
        os.rename(f[:-4] + '.xml', f[:-4] + '_D.xml')
    else:
        os.rename(f, f[:-4] + '_N.jpg')
        os.rename(f[:-4] + '.xml', f[:-4] + '_N.xml')
