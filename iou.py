from configparser import SafeConfigParser
import os
import os.path
import xml.etree.ElementTree as ET

parser = SafeConfigParser()
parser.read('config.txt')
gt_path = parser.get('path', 'gt_path')
predict_path = parser.get('path', 'predict_path')
gt_list = []
predict_list = []


def write_gt():
    source_dir = gt_path
    os.chdir(source_dir)
    list_dir = os.listdir()
    list_dir = [file for file in list_dir]
    list_dir = sorted(list_dir)
    for filename in list_dir:
        file_name, file_extension = os.path.splitext(filename)
        if file_extension == '.xml':
            gt_list.append(file_name)
            tree = ET.parse(file_name + '.xml')
            root = tree.getroot()
            xmin = root.findtext('object/bndbox/xmin')
            xmax = root.findtext('object/bndbox/xmax')
            ymax = root.findtext('object/bndbox/ymax')
            ymin = root.findtext('object/bndbox/ymin')
            with open(gt_path + '/GT.txt', 'a') as f:
                f.write(
                    "{} \n xmax = {} \n xmin = {} \n ymax = {} \n ymin = {} \n \n".format('[' + file_name + ']', xmax,
                                                                                          xmin, ymax, ymin))


def write_predict():
    source_dir = predict_path
    os.chdir(source_dir)
    list_dir = os.listdir()
    list_dir = [file for file in list_dir]
    list_dir = sorted(list_dir)
    for filename in list_dir:
        file_name, file_extension = os.path.splitext(filename)
        if file_extension == '.xml':
            predict_list.append(file_name.rsplit('_', 1)[0])
            tree = ET.parse(file_name + '.xml')
            root = tree.getroot()
            xmin = root.findtext('object/bndbox/xmin')
            xmax = root.findtext('object/bndbox/xmax')
            ymax = root.findtext('object/bndbox/ymax')
            ymin = root.findtext('object/bndbox/ymin')
            with open(predict_path + '/Predict.txt', 'a') as f:
                f.write(
                    "{} \n xmax = {} \n xmin = {} \n ymax = {} \n ymin = {} \n \n".format('[' + file_name.rsplit('_', 1)[0] + ']', xmax,
                                                                                          xmin, ymax, ymin))


def calculate_iou():
    # Get files that only has intersection between ground truth and prediction
    intersect = sorted((set(gt_list).intersection(set(predict_list))))
    print(intersect)
    for intersect_list in intersect:
        # Write ground truth values to text file
        parser1 = SafeConfigParser(strict=True)
        parser1.read(gt_path + '/GT.txt')
        gt_xmax = parser1.get(intersect_list, 'xmax')
        gt_ymax = parser1.get(intersect_list, 'ymax')
        gt_xmin = parser1.get(intersect_list, 'xmin')
        gt_ymin = parser1.get(intersect_list, 'ymin')

        # Write prediction values to text file
        parser2 = SafeConfigParser(strict=True)
        parser2.read(predict_path + '/Predict.txt')
        predict_xmax = parser2.get(intersect_list, 'xmax')
        predict_ymax = parser2.get(intersect_list, 'ymax')
        predict_xmin = parser2.get(intersect_list, 'xmin')
        predict_ymin = parser2.get(intersect_list, 'ymin')

        gtbox = [int(gt_xmin), int(gt_ymin), int(gt_xmax), int(gt_ymax)]
        predictbox = [int(predict_xmin), int(predict_ymin), int(predict_xmax), int(predict_ymax)]

        # Write IoU values to a text file
        with open(predict_path + '/IoU.txt', 'a') as f:
            f.write("File: {}, IoU: {} \n".format(intersect_list, bb_intersection_over_union(gtbox, predictbox)))
        # print(bb_intersection_over_union(gtbox, predictbox))


def bb_intersection_over_union(boxA, boxB):
    # determine the (x, y)-coordinates of the intersection rectangle
    xA = max(boxA[0], boxB[0])
    yA = max(boxA[1], boxB[1])
    xB = min(boxA[2], boxB[2])
    yB = min(boxA[3], boxB[3])

    # compute the area of intersection rectangle
    interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)

    # compute the area of both the prediction and ground-truth
    # rectangles
    boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
    boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)

    # compute the intersection over union by taking the intersection
    # area and dividing it by the sum of prediction + ground-truth
    # areas - the intersection area
    iou = interArea / float(boxAArea + boxBArea - interArea)
    # print(iou)

    # return the intersection over union value
    return iou


if __name__ == '__main__':
    # bb_intersection_over_union([10, 20, 20, 30], [10, 20, 21, 30])
    write_gt()
    write_predict()
    calculate_iou()

