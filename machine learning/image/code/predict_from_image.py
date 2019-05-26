#!/usr/bin/env python2
import os
import sys
import traceback
import Tkinter as tk
import cv2
from tetos import *
from sklearn.externals import joblib

from common.config import get_config
from common.image_transformation import apply_image_transformation
from common.image_transformation import resize_image


def get_image_from_label(label):
    testing_images_dir_path = get_config('testing_images_dir_path')
    image_path = os.path.join(testing_images_dir_path, label, '001.jpg')
    image = cv2.imread(image_path)
    return image


def mainimage():
    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,50)
    fontScale              = 1
    fontColor              = (255,255,255)
    lineType               = 2
    model_name = "svm"
    if model_name not in ['svm']:
        print("Invalid model-name '{}'!".format(model_name))
        return

    print("Using model '{}'...".format(model_name))

    model_serialized_path = get_config(
        "model_{}_serialized_path".format(model_name))
    print("Model deserialized from path '{}'".format(model_serialized_path))
    classifier_model = joblib.load(model_serialized_path)
    import tkFileDialog
    tk.Tk().withdraw()
    path=tkFileDialog.askopenfile()
    img=cv2.imread(path.name)
    frame = resize_image(img, 400)
    image=frame
    frame=cv2.resize(img,(50,50))

    
    try:    
            frame = apply_image_transformation(frame)
            frame_flattened = frame.flatten()
            
            print classifier_model
            predicted_labels = classifier_model.predict(frame_flattened)
            print("Predicted label = {}".format(predicted_labels))
            cv2.putText(image,str(predicted_labels),bottomLeftCornerOfText,font, 
            fontScale,fontColor,lineType)
            cv2.imshow("frame",image)
            key=cv2.waitKey(2)
            if key==27:
              cv2.destroyAllWindows()
    except Exception:
            exception_traceback = traceback.format_exc()
            print("Error while applying image transformation with the following exception trace:\n{}".format(
                exception_traceback))
    cv2.waitKey(0)
    print "The program completed successfully !!"


##if __name__ == '__main__':
mainimage()
