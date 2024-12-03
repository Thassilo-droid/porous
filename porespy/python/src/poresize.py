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


dataset_path = r'..\\non_inverted' # Choose the correct path to dataset (Folder with .pngs)

# Load the dataset into a 3D numpy array
image_stack = load_image_to_array(dataset_path)

print("Shape of image stack:", image_stack.shape)

# Filter binar_image with ps.filters.porosimetry filter
filtered_image = ps.filters.porosimetry(
    im=image_stack,
    sizes=25,  # Example: scalar for auto-detection of size range
    access_limited=True,  # Default: simulates real-world porosimetry
    mode='hybrid',  # Default mode
    divs=1  # No parallel chunking
)

# Calculate poresize distribution with ps.metrics.pore_size_distribution (with log = False); bins = 100 (intervals of datapoints taken)
data = ps.metrics.pore_size_distribution(im=filtered_image, log=False, bins = 500)

# Display data; pdf = Probability Density Function; cdf = Cumulative Density Function
fig, ax = plt.subplots(1, 3, figsize=[20, 4])

# PDF plot
ax[0].plot(data['bin_centers'], data['pdf'], label='PDF', color='blue')
ax[0].set_title("Probability Density Function")
ax[0].set_xlabel("Pore radius [pixel]")
ax[0].set_ylabel("Density")
ax[0].legend()

# CDF plot
ax[1].plot(data['bin_centers'], data['cdf'], label='CDF', color='green')
ax[1].set_title("Cumulative Density Function")
ax[1].set_xlabel("Pore radius [pixel]")
ax[1].set_ylabel("Cumulative Probability")
ax[1].legend()

# Bar plot
ax[2].bar(data['bin_centers'], data['pdf'], width=data['bin_widths'], edgecolor='k', label='Bar Plot')
ax[2].set_title("Bar Plot (PDF)")
ax[2].set_xlabel("Pore radius [pixel]")
ax[2].set_ylabel("Density")
ax[2].legend()

plt.tight_layout()
plt.show()