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
#filtered_image = ps.filters.local_thickness(binary_image)

# Lokale Dicke berechnen (Porenradius)
lt = ps.filters.local_thickness(binary_image)

# Umwandlung in physikalische Einheiten und Durchmesser
voxel_size = 1  # Falls z.B. ein Voxel = 10 µm ist, setzen Sie voxel_size=10
radii = lt[lt > 0] * voxel_size  # Porenradius in µm
diameters = radii * 2  # Umrechnung von Radius zu Durchmesser

# Benutzerdefinierte Intervalle: 0 bis 60 µm, in Schritten von 5 µm
bin_edges = np.arange(0, 65, 5)  # 0, 5, 10, ..., 60 µm
hist, _ = np.histogram(diameters, bins=bin_edges, density=False)
hist_percentage = hist / hist.sum() * 100  # In Prozent umwandeln
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2  # Mittelpunkte der Intervalle

# Plotten
plt.figure(figsize=(8, 5))
plt.bar(bin_centers, hist_percentage, width=np.diff(bin_edges), edgecolor='k', alpha=0.7)
plt.xlabel('Porendurchmesser (µm)')
plt.ylabel('Wahrscheinlichkeit (%)')
plt.title('Wahrscheinlichkeit für Porengrößen (0 bis 60 µm)')
plt.grid(alpha=0.3)
plt.show()

