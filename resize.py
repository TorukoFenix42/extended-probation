from PIL import Image
import os, sys
import xml.etree.ElementTree as ET
from lxml import etree

<<<<<<< HEAD
<<<<<<< HEAD
load_path = '/home/load_path/'
save_path = '/home/save_path/'
=======
load_path = '/home/rnd/Downloads/tester/'
save_path = '/home/rnd/Downloads/tester1/'
>>>>>>> 5592f8e... Initial commit
=======
load_path = '/home/load_path/'
save_path = '/home/save_path/'
>>>>>>> 34fe968... Update some configs and README

def resize():
    for (dirpath, dirnames, filenames) in os.walk(load_path):
        source_dir = load_path
        os.chdir(source_dir)
        list_dir = os.listdir()
        list_dir = [file for file in list_dir]
        list_dir = sorted(list_dir)
        for filename in list_dir:
            file_name, file_extension = os.path.splitext(filename)
            if file_extension == '.jpg':
                im = Image.open(load_path + file_name + file_extension)
                imResize = im.resize((1280, 720), Image.ANTIALIAS)
                imResize.save(save_path + file_name + '_720p.jpg', 'JPEG', quality=100)

            elif (file_extension == '.xml'):
                tree = ET.parse(file_name + '.xml')
                root = tree.getroot()
                xmin = root.findtext('object/bndbox/xmin')
                xmax = root.findtext('object/bndbox/xmax')
                ymax = root.findtext('object/bndbox/ymax')
                ymin = root.findtext('object/bndbox/ymin')
                write2xml(im, [(int(xmin) * 2 / 3), (int(ymin) * 2 / 3), (int(xmax) * 2 / 3), (int(ymax) * 2 / 3)],
                          save_path + file_name + "_720p.jpg", save_path + file_name + "_720p.xml")

def write2xml(arr_img, bboxes_, imgname, save_dir):
    # Tree top
    annotate = etree.Element("annotation")

    # Folder node
    folder = etree.SubElement(annotate, "folder")
    folder.text = save_dir

    # Filename node
    fname = etree.SubElement(annotate, "filename")
    fname.text = imgname.split('/')[-1]

    # Path node
    path = etree.SubElement(annotate, "path")
    path.text = imgname

    # Source node
    source = etree.SubElement(annotate, "source")
    db = etree.SubElement(source, "database")
    db.text = 'Unknown'

    # Size node
    size = etree.SubElement(annotate, "size")
    width = etree.SubElement(size, "width")
    width.text = str(1280)
    height = etree.SubElement(size, "height")
    height.text = str(720)
    depth = etree.SubElement(size, "depth")
    depth.text = str(3)

    # Segmented node
    segmented = etree.SubElement(annotate, "segmented")
    segmented.text = str(0)

    [xmin, ymin, xmax, ymax] = bboxes_
    # Object node(s)
    obj = etree.SubElement(annotate, "object")
    obj_name = etree.SubElement(obj, "name")
    obj_name.text = 'VLP'
    obj_pose = etree.SubElement(obj, "pose")
    obj_pose.text = 'Unspecified'
    obj_truncated = etree.SubElement(obj, "truncated")
    obj_truncated.text = str(0)
    obj_difficult = etree.SubElement(obj, "difficult")
    obj_difficult.text = str(0)
    obj_bndbox = etree.SubElement(obj, "bndbox")
    obj_bndbox_xmin = etree.SubElement(obj_bndbox, "xmin")
    obj_bndbox_xmin.text = str(int(xmin))

    obj_bndbox_ymin = etree.SubElement(obj_bndbox, "ymin")
    obj_bndbox_ymin.text = str(int(ymin))

    obj_bndbox_xmax = etree.SubElement(obj_bndbox, "xmax")
    obj_bndbox_xmax.text = str(int(xmax))

    obj_bndbox_ymax = etree.SubElement(obj_bndbox, "ymax")
    obj_bndbox_ymax.text = str(int(ymax))

    # Write xml file
    et = etree.ElementTree(annotate)
    annotfile_dir = save_dir
    # + imgname.split('/')[-1].split(".")[0] + '.xml'
    # print(annotfile_dir)
    et.write(annotfile_dir, pretty_print=True)

if __name__ == '__main__':
    resize()
