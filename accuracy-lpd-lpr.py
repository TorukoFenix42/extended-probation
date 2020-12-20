from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import cv2
import os, glob, sys
os.environ["GLOG_minloglevel"] = "2"
import shutil
import datetime
import time
import argparse
import caffe
import numpy as np 
from net import lpd_ssd
from net import lpr_crnn
from utils import inference_configuration
from utils import image_preprocess
from utils import database
from utils import xmlwriter
from fuzzywuzzy import fuzz

correct_prediction = []
wrong_prediction = []
ground_truth_list = []

def arg_parser(argv):
    parser = argparse.ArgumentParser()
    # TODO: Create multiple config file for respective project
    parser.add_argument("--c", "--config", metavar='CONFIGURATION FILE PATH', type=str,
                        help='Path to configuration file')
    return parser.parse_args(argv)


def check_boundary(xmin, ymin, xmax, ymax, img_H, img_W):
    if xmin < 0:
        xmin = 0
    if ymin < 0:
        ymin = 0
    if xmax > img_W-1:
        xmax = img_W-1
    if ymax > img_H-1:
        ymax = img_H-1
    return xmin, ymin, xmax, ymax


if __name__ == '__main__':
    args = arg_parser(sys.argv[1:])

    # Read configurations
    infer_config = inference_configuration.NetConfig(args)
    vd_models, pd_models, lpr_models, conf_thres, virtual_loop, gpu_id, fps, display, db, db_vimg_dir, db_pimg_dir, \
        comm, input_source, video_name, video_stream, http_info_file, rtsp_stream, http_images_dir, dustbin_img_dir, \
        img_dir, img_past_dir, img_vlp = infer_config.get_config()

    caffe.set_device(gpu_id)
    caffe.set_mode_gpu()

    print('-LPD LPR Engine Initialization-')
    # Initialize image preprocess
    img_prep = image_preprocess.ImagePreprocess()

    # Initialize Auto-labeling
    write_xml = xmlwriter.XML()

    # Initialize Caffe engine, prototxt, caffemodel
    lpd = lpd_ssd.PlateDetection(pd_models)
    lpr = lpr_crnn.PlateRecognition(lpr_models)
    if db == 0:
        database_ = database.None_DB()
    elif db == 1:
        database_ = database.PostgreSQL()
    elif db == 2:
        database_ = database.MSSQL()

    print('Image sink ... ', end='')
    img_paths = [img_dir, img_past_dir, img_vlp]
    for i, folder in enumerate(img_paths):
        if not os.path.exists(img_paths[i]):
            print("\n{0} are not found ... ".format(folder))
            break
    print("Checked \n")
    print("Start LPD LPR inference")

    count = 0
    print('-----------------------------------------------------------------------------------------------------')
    # print('Date\t\t\t', 'Image\t\t\t\t\t\t\t', '\tNumber Plate')
    master_start_time = time.time()
    while True:
        # try:
        for image_file in sorted(glob.glob(os.path.join(img_dir, '*.jpg'))):
	    #split image file from extension and get ground truth result
            image_gt, file_extension = os.path.splitext(image_file)
            image_gt = image_gt.split('_')[-1]
            ground_truth_list.append(image_gt)

            time.sleep(0.01)
            # Initialize result placeholder
            lpr_result = '0000'
            bbox = 50, 50, 100, 100
            timestamp = datetime.datetime.now()
            timestamp_str = timestamp.strftime("%Y%m%d-%H%M%S-%f")[:-3]
            print("\nTime: {0}".format(timestamp_str))
            print("Vehicle: {0}".format(image_file))
            img = cv2.imread(image_file)
            img_H, img_W, img_C = img.shape
            proc_start_time = time.time()
            plate_roi = lpd.detect_plate(img, conf_thresh=conf_thres[1])
            if plate_roi:
                for plate in plate_roi:
                    xmin = int(round(plate[0] * img_W))
                    ymin = int(round(plate[1] * img_H))
                    xmax = int(round(plate[2] * img_W))
                    ymax = int(round(plate[3] * img_H))
                    xmin, ymin, xmax, ymax = check_boundary(xmin, ymin, xmax, ymax, img_H, img_W)
                    bbox = xmin, ymin, xmax, ymax

                plate_img = img[ymin:ymax, xmin:xmax]
                plate_H, plate_W, plate_C = plate_img.shape
                if plate_W and plate_H > 0:
                    if plate_W/plate_H < 2.2:
                        print("Type: Double Line Plate")
                        ocr_img = img_prep.concat(plate_img, plate_H, plate_W, plate_C)
                    else:
                        print("Type: Single Line Plate")
                        ocr_img = plate_img
                else:
                    ocr_img = np.zeros((32, 128, 3))
                lpr_result = lpr.recognizeNumberPlate(ocr_img, conf_thresh=conf_thres[2])
            else:
                plate_img = np.zeros((32, 128, 3))

            print("LPR: {0}".format(lpr_result))
            proc_time = time.time() - proc_start_time
            lane_name = image_file.split('/')[-1].split('_')[0]
            inferred_img_name = image_file.split('/')[-1].split('.')[0] + '_' + lpr_result + '.jpg'
            
            #calculate ratio between predicted result and ground truth image
            rat = fuzz.ratio(image_gt, lpr_result)
            if(rat >= 100):
                correct_prediction.append(lpr_result)
            else:
                wrong_prediction.append(lpr_result)
            
            # TODO: Archive the old folder
            # inferred_dir_root = img_past_dir + image_file.split('/')[-1].split('.')[0]
            # print(inferred_dir_root)
            # inferred_dir = inferred_dir_root.split('-')[0] + inferred_img_name.split('-')[1] + '/'
            # VLP image
            vlp_image = img_vlp + inferred_img_name
            # Vehicle image
            new_img_name = img_past_dir + inferred_img_name
            # print(inferred_dir)
            # print(image_file)
            shutil.move(image_file, new_img_name)
            # write_xml()
            cv2.imwrite(vlp_image, plate_img)
            database_.store_data(inferred_img_name, lpr_result, db_vimg_dir, db_pimg_dir, proc_time)
            write_xml.write2xml(img, bbox, new_img_name, img_past_dir)
            count += 1
            print("Count: ", count)
            print("Cumulative Accuracy = {0:.2f}".format(((len(correct_prediction)) / (len(ground_truth_list)) * 100)))

        
        print("Elapsed Time = {0:.3f}".format(time.time() - master_start_time), end='\r')

        # except KeyboardInterrupt:
        #     print("Inference Interrupted by keyboard")