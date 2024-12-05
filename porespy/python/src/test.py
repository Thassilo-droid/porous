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

#dataset_path = "C:\\Users\\thass\\Desktop\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted"
dataset_path = "V:\\Horn, Thassilo\\BA\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted"

# Load the dataset into a 3D numpy array
image_stack = load_image_to_array(dataset_path)

# Filter image with porespy.filters
im = ps.filters.local_thickness(image_stack)

radii = im[im > 0].flatten()  # Alle Werte in einer 1D-Liste

# Sort and count unique values in radii array
unique_values, counts = np.unique(radii, return_counts=True)

# Calculate relative number
total_count = len(radii)
relative_frequencies = counts / total_count

# Save results in x and y list
x = unique_values.tolist() # List of unique values
y = relative_frequencies.tolist() # List of relative number

y_p =[]

for el in y:
    y_p.append(el*100) 

print(x)
print("------------------------")
print(y)

print(f"radii.shape:{radii.shape}")
print(f"radii.type:{type(radii)}")

print(radii)

plt.subplot(1,2,1)
plt.hist(radii, bins=75, density=True, edgecolor='black')  # Bins einstellen
plt.xlabel('Porenradius (Pixel)')
plt.ylabel('Wahrscheinlichkeit')
plt.title('Histogramm der Porenradien (in Pixeln)')


plt.subplot(1,2,2)
plt.figure(figsize=(10, 6))
plt.bar(x, y, width = 0.4, color = 'b', label = "Data Points", alpha = 0.7)
plt.title("Barplot of pore size", fontsize = 14)
plt.xlabel("Pore radius [pixel]")
plt.ylabel("Percent Volume in range [%]")
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.legend()



plt.tight_layout()
plt.show()