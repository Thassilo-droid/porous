import os
import numpy as np
import porespy as ps
from skimage.io import imread
import matplotlib.pyplot as plt

# Path to original image
image_path = r'..\\..\\daten\\30ppi__rec_voi_1642.png'

# Set image to original image
image = imread(os.path.join(image_path))

# Binarize image (only True and False values)
binary_image = image < 0.5

# Filter binar_image with ps.filters.porosimetry filter
filtered_image = ps.filters.porosimetry(binary_image)


# Calculate poresize distribution with ps.metrics.pore_size_distribution (with log = False); bins = 100 (intervals of datapoints taken)
data = ps.metrics.pore_size_distribution(im=filtered_image, log=False, bins = 500)

# Display data; pdf = Probability Density Function; cdf = Cumulative Density Function
fig, ax = plt.subplots(1, 5, figsize=[20, 4])

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

# Display binary image
ax[3].imshow(((binary_image)*255).astype(np.uint8), cmap='gray')
ax[3].set_title("Binary Image")
ax[3].axis('off')

# Display image
ax[4].imshow(image)
ax[4].set_title("Image")
ax[4].axis('off')


plt.tight_layout()
plt.show()

