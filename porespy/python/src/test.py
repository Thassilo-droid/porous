import os
import numpy as np
import porespy as ps
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

def load_image_to_array(folder_path):
    # Get a sorted list of the PNG files in the folder
    file_list = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    # Load and threshold images (binarize) and stack them into a 3D numpy array
    images = []

    for file in file_list:

        # Load image
        image = imread(os.path.join(folder_path, file))

        # Convert to greayscale to remove 4th dimension
        if image.ndim == 3 and image.shape[-1] == 3:
            image = rgb2gray(image)

        # Threshold to binarize the image (<0.5)
        binary_image = image < 0.5

        # Add binarized images to images[] list
        images.append(binary_image)
    
    return np.array(images)

dataset_path = "C:\\Users\\thass\\Desktop\\non_inverted"




