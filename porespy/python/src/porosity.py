import os
import numpy as np
import porespy as ps
from skimage.io import imread

def load_image_to_array(folder_path):
    # Get a sorted list of the PNG files in the folder
    file_list = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    # Load and threshold images (binarize) and stack them into a 3D numpy array
    images = []

    for file in file_list:

        # Load image
        image = imread(os.path.join(folder_path, file))

        # Threshold to binarize the image (>0.5)
        binary_image = image < 0.5

        # Add binarized images to images[] list
        images.append(binary_image)
    
    return np.array(images)

def calcualte_porosity(image_stack):
    # Calculate porosity using PoreSpy
    porosity = ps.metrics.porosity(image_stack)
    return porosity

# Path to your dataset
dataset_path = r'..\\non_inverted' # Choose the correct path to dataset (Folder with .pngs)

# Load the dataset into a 3D numpy array
image_stack = load_image_to_array(dataset_path)

# Calculate porosity
porosity = calcualte_porosity(image_stack)

print("Porosity of the dataset: ", porosity)