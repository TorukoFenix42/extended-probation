import xml.etree.ElementTree as ET
from lxml import etree


class XML(object):

    def _init_(self):
        print("XML Writer ... Checked")

    def write2xml(self, arr_img, bboxes_, imgname, save_dir):
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
        annotfile_dir = save_dir + imgname.split('/')[-1].split(".")[0] + '.xml'
        # print(annotfile_dir)
        et.write(annotfile_dir, pretty_print=True)
		
		write_xml.write2xml(img, bbox, new_img_name, img_past_dir)