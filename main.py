import cv2
import numpy as np
import os
from shutil import move

def sharp(image_path, threshold=100):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    laplacian_var = cv2.Laplacian(image, cv2.CV_64F).var()
    return laplacian_var >= threshold

def sort(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for filename in os.listdir(source_folder):
        if filename.lower().endswith(('jpg', 'jpeg', 'png', 'bmp', 'tiff')):
            image_path = os.path.join(source_folder, filename)
            if sharp(image_path):
                os.rename(image_path, os.path.join(destination_folder, filename))

source_folder = 'Images'
destination_folder = 'Unsharpened'
sort(source_folder, destination_folder)