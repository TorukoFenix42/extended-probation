import os
import shutil
from configparser import SafeConfigParser
import os
import xml.etree.ElementTree as ET
from os import walk
from lxml import etree
import cv2

parser = SafeConfigParser()
parser.read('config.txt')

# jpg_path = parser.get('path', 'jpg_path')
# xml_path = parser.get('path', 'xml_path')
<<<<<<< HEAD
xml_path = "/home/XML_Label"
jpg_path = "/home/JPG_Images"
=======
xml_path = "/media/imageDB/LPR/0_NewData/lpd-003-my-r/VOCdevkit/VOC2007/Annotations"
jpg_path = "/media/imageDB/LPR/0_NewData/lpd-003-my-r/VOCdevkit/VOC2007/JPEGImages"
>>>>>>> 5592f8e... Initial commit
# jpg_list = []
xml_list = []
anomalies = []


def createfolder(whatever):
    try:
        os.makedirs(whatever)
    except OSError:
        pass


def get_xml(xml_path):
    source_dir = xml_path
    os.chdir(source_dir)
    list_dir = os.listdir()
    list_dir = [file for file in list_dir]
    list_dir = sorted(list_dir)
    createfolder(xml_path + '/xml')
    for filename in list_dir:
        file_name, file_extension = os.path.splitext(filename)
        if (file_extension == ('.xml')):
            tree = ET.parse(file_name + '.xml')
            root = tree.getroot()
            xmin = root.findtext('object/bndbox/xmin')
            xmax = root.findtext('object/bndbox/xmax')
            ymax = root.findtext('object/bndbox/ymax')
            ymin = root.findtext('object/bndbox/ymin')
            img = cv2.imread(jpg_path + "/" + file_name + '.jpg')
            if (int(xmax) - int(xmin) == 0) or (int(ymax) - int(ymin) == 0):
                shutil.move(xml_path + "/" + file_name + ".xml", xml_path + "/xml/" + file_name + ".xml")
            elif (int(xmax) - int(xmin)) * (int(ymax) - int(ymin)) < 10:
                shutil.move(xml_path + "/" + file_name + ".xml", xml_path + "/xml/" + file_name + ".xml")
            elif (int(xmax) - int(xmin)) / (int(ymax) - int(ymin)) >= 10 or (int(ymax) - int(ymin)) / (
                    int(xmax) - int(xmin)) >= 10:
                shutil.move(xml_path + "/" + file_name + ".xml", xml_path + "/xml/" + file_name + ".xml")
            elif int(xmax) < 0 or int(xmin) < 0 or int(ymax) < 0 or int(ymin) < 0:
                shutil.move(xml_path + "/" + file_name + ".xml", xml_path + "/xml/" + file_name + ".xml")
            elif int(xmax) > img.shape[1] or int(ymax) > img.shape[0]:
                shutil.move(xml_path + "/" + file_name + ".xml", xml_path + "/xml/" + file_name + ".xml")


if __name__ == '__main__':
    get_xml(xml_path)