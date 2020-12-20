import os
import shutil
from configparser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.txt')

jpg_path = parser.get('path', 'jpg_path')
xml_path = parser.get('path', 'xml_path')

<<<<<<< HEAD
# jpg_path = "/home/path"
# xml_path = "/home/path"
=======
# jpg_path = "/media/imageDB/LPR/5_testset/WCE/lpd/Day/GT"
# xml_path = "/media/imageDB/LPR/5_testset/WCE/lpd/Day/GT"
>>>>>>> 5592f8e... Initial commit

jpg_list = []
xml_list = []
anomalies = []

def get_jpg(jpg_path):
    for (dirpath, dirnames, filenames) in os.walk(jpg_path):
        source_dir = jpg_path
        os.chdir(source_dir)
        list_dir = os.listdir()
        list_dir = [file for file in list_dir]
        list_dir = sorted(list_dir)
        for filename in list_dir:
            file_name, file_extension = os.path.splitext(filename)
            if (file_extension == ('.jpg')):
                jpg_list.append(file_name)
            elif file_extension == ('.xml'):
                continue
            # else:
            #     other_list.append(file_name + file_extension)
    return jpg_list

def get_xml(xml_path):
    for (dirpath, dirnames, filenames) in os.walk(xml_path):
        source_dir = xml_path
        os.chdir(source_dir)
        list_dir = os.listdir()
        list_dir = [file for file in list_dir]
        list_dir = sorted(list_dir)
        for filename in list_dir:
            file_name, file_extension = os.path.splitext(filename)
            if (file_extension == ('.xml')):
                xml_list.append(file_name)
            elif file_extension == ('.jpg'):
                continue
            # else:
            #     other_list.append(file_name + file_extension)
    return xml_list

def createfolder(whatever):
    try:
        os.makedirs(whatever)
    except OSError:
        pass

if __name__ == '__main__':
    get_jpg(jpg_path)
    get_xml(xml_path)
    print("JPEG list: " + str(jpg_list))
    print("Length of JPEG list: " + str(len(jpg_list)))
    print("XML list: " + str(xml_list))
    print("Length of XML list: " + str(len(xml_list)))
    anomalies = sorted((set(jpg_list).symmetric_difference(set(xml_list))))
    jpg_out = sorted((set(anomalies).intersection(set(jpg_list))))
    xml_out = sorted((set(anomalies).intersection(set(xml_list))))
    if (len(jpg_out) > 0):
        createfolder(jpg_path + '/jpeg')
        with open(jpg_path + '/jpeg/JPG_anomalies.txt', 'w') as f:
            for item in jpg_out:
                f.write("%s.jpg\n" % item)
                shutil.move(jpg_path + "/" + "%s.jpg" % item, jpg_path + "/jpeg/" + "%s.jpg" % item)
        print("JPEG list anomalies: " + str(jpg_out))

    if (len(xml_out) > 0):
        createfolder(xml_path + '/xml')
        with open(xml_path + '/xml/XML_anomalies.txt', 'w') as f:
            for item in xml_out:
                f.write("%s.xml\n" % item)
                shutil.move(xml_path + "/" + "%s.xml" % item, xml_path + "/xml/" + "%s.xml" % item)
        print("XML list anomalies: " + str(xml_out))