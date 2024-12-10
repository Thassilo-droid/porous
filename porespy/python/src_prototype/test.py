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

dataset_path = "V:\\Horn, Thassilo\\BA\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted" # Uni
#dataset_path = "C:\\Users\\thass\\Desktop\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted" # Privat

# Load the dataset into a 3D numpy array
image_stack = load_image_to_array(dataset_path)

size_list = []
for i in range (1, 101):
    size_list.append(i)

print(size_list)

# Filter image with porespy.filters
im = ps.filters.local_thickness(image_stack, sizes = size_list)

radii = im[im > 0].flatten()  # Alle Werte in einer 1D-Liste

# Sort and count unique values in radii array
unique_values, counts = np.unique(radii, return_counts=True)

# Calculate relative number
total_count = len(radii)
relative_frequencies = counts / total_count

# Save results in x and y list
x = unique_values.tolist() # List of unique values
y = relative_frequencies.tolist() # List of relative number

x_d = [] # Durchmesser = 2 * Radius
y_p =[] # Für Prozent Anteil * 100


for el in x:
    x_d.append(el*2)

for el in y:
    y_p.append(el*100) 


print(x)
print("------------------------------------------------------------------------------------------------------------------------")
print(y_p)
print("------------------------------------------------------------------------------------------------------------------------")

outputfile = "test_output.txt"
with open(outputfile, "w") as f:
    for diameter, probability in zip(x_d, y_p):
            f.write(f"{diameter}\t{probability:.2f}\n")


plt.bar(x_d, y_p, color="green")

plt.title("Barplot of poresize", fontsize=20)
plt.xlabel("Pore Diameter [pixel]", fontsize=18)  # X-axis label
plt.ylabel("Percentage [%]", fontsize=18)  # Y-axis label
plt.grid(axis='y', linestyle='--')  # Horizontale Linien für bessere Lesbarkeit
plt.legend(fontsize = 18)  # Add legend
plt.tight_layout()  # Adjust layout
plt.show()