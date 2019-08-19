import cv2
import os
import xml.etree.ElementTree as ET
from os import walk
from lxml import etree
import argparse

def init_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('--load_dir', type = str, help = 'Directory to crop images, include a "/" at EOL.')
	parser.add_argument('--save_dir', type = str, help = 'Directory to save cropped images, include a "/" at EOL.')
	parser.print_help()
	
	return parser.parse_args()

def get_img(path, save_path):
	source_dir = path
	os.chdir(source_dir)
	list_dir = os.listdir()
	list_dir = [file for file in list_dir]
	list_dir = sorted(list_dir)
	# print(list_dir)
	for filename in list_dir:
		file_name, file_extension = os.path.splitext(filename)
		if(file_extension == ('.jpg')):
			image = cv2.imread(filename)
			if(image.shape[0] < 200):
				# print(filename)
				# No Crop
				tree = ET.parse(file_name + '.xml')
				root = tree.getroot()
				xmin = root.findtext('object/bndbox/xmin')
				xmax = root.findtext('object/bndbox/xmax')
				ymax = root.findtext('object/bndbox/ymax')
				ymin = root.findtext('object/bndbox/ymin')
				# print(xmin, xmax, ymin, ymax)
			
			# Car image with bonnet
			elif(image.shape[0] > 200) and (image.shape[0] < 370):
				# print(filename)
				tree = ET.parse(file_name + '.xml')
				root = tree.getroot()
				xmin = root.findtext('object/bndbox/xmin')
				xmax = root.findtext('object/bndbox/xmax')
				ymax = root.findtext('object/bndbox/ymax')
				ymin = root.findtext('object/bndbox/ymin')
				# print(xmin, xmax, ymin, ymax)
				
				# Crop 50 %
				offset = int(image.shape[0]/2)
				if offset > int(ymin):
					offset = int(ymin)
				cropped = image[offset:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_1.jpg", cropped)
				write2xml(cropped, [xmin, str(int(ymin) - offset), xmax, str(int(ymax) - offset)], file_name + "_1.jpg", save_path + file_name + "_1.xml")
			
			# Car image with bonnet and windscreen
			elif(image.shape[0] > 370) and (image.shape[0] < 720):
				# print(filename)
				tree = ET.parse(file_name + '.xml')
				root = tree.getroot()
				xmin = root.findtext('object/bndbox/xmin')
				xmax = root.findtext('object/bndbox/xmax')
				ymax = root.findtext('object/bndbox/ymax')
				ymin = root.findtext('object/bndbox/ymin')
				# print(xmin, xmax, ymin, ymax)
				
				# Crop 50 %
				offset = int(image.shape[0]/2)
				if offset > int(ymin):
					offset = int(ymin)
				cropped = image[offset:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_1.jpg", cropped)				
				write2xml(cropped, [xmin, str(int(ymin) - offset), xmax, str(int(ymax) - offset)], file_name + "_1.jpg", save_path + file_name + "_1.xml")
				
				# Crop 71 %
				offset2 = int(5*image.shape[0]/7)
				if offset2 > int(ymin):
					offset2 = int(ymin)
				cropped2 = image[offset2:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_2.jpg", cropped2)
				write2xml(cropped2, [xmin, str(int(ymin) - offset2), xmax, str(int(ymax) - offset2)], file_name + "_2.jpg", save_path + file_name + "_2.xml")
				
			# Whole car
			else:
				# print(filename)
				tree = ET.parse(file_name + '.xml')
				root = tree.getroot()
				xmin = root.findtext('object/bndbox/xmin')
				xmax = root.findtext('object/bndbox/xmax')
				ymax = root.findtext('object/bndbox/ymax')
				ymin = root.findtext('object/bndbox/ymin')
				# print(xmin, xmax, ymin, ymax)
				
				# Crop 50 %
				offset = int(image.shape[0]/2)
				if offset > int(ymin):
					offset = int(ymin)
				cropped = image[offset:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_1.jpg", cropped)				
				write2xml(cropped, [xmin, str(int(ymin) - offset), xmax, str(int(ymax) - offset)], file_name + "_1.jpg", save_path + file_name + "_1.xml")
				
				# Crop 71 %
				offset2 = int(5*image.shape[0]/7)
				if offset2 > int(ymin):
					offset2 = int(ymin)
				cropped2 = image[offset2:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_2.jpg", cropped2)
				write2xml(cropped2, [xmin, str(int(ymin) - offset2), xmax, str(int(ymax) - offset2)], file_name + "_2.jpg", save_path + file_name + "_2.xml")
				
				# Crop 83 %
				offset3 = int(5*image.shape[0]/6)
				if offset3 > int(ymin):
					offset3 = int(ymin)
				cropped3 = image[offset3:int(image.shape[0]),0:int(image.shape[1])]
				cv2.imwrite(save_path + file_name + "_3.jpg", cropped3)
				write2xml(cropped3, [xmin, str(int(ymin) - offset3), xmax, str(int(ymax) - offset3)], file_name + "_3.jpg", save_path + file_name + "_3.xml")
		else:
		   continue
		
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
        width.text = str(arr_img.shape[1])
        height = etree.SubElement(size, "height")
        height.text = str(arr_img.shape[0])
        depth = etree.SubElement(size, "depth")
        depth.text = str(arr_img.shape[2])

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
	args = init_args()
	get_img(args.load_dir, args.save_dir)
