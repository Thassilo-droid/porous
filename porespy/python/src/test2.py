import os
import numpy as np
import porespy as ps
from skimage.io import imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# Path to original image
image_path = r'..\\..\\daten\\30ppi__rec_voi_1642.png'

# Set image to original image
image = imread(os.path.join(image_path))

# Binarize image (only True and False values)
binary_image = image < 0.5

# grayscale
grayscale_image = rgb2gray(binary_image)

# Lokale Dicke berechnen (Porenradius)
im = ps.filters.local_thickness(grayscale_image)


print(type(im))
print("------------------")
print(im)
print("------------------")
print(im.shape)
print("------------------")

# Alle Porengrößen (größer als 0) extrahieren und ein Histogramm erstellen
radii = im[im > 0].flatten()  # Alle Werte in einer 1D-Liste
radii[145000:150000] = 57
print(f"radii:{radii}")
print(f"radii.shape:{radii.shape}")

a = np.array([])

c = 0


for i in range(len(radii)):
    if radii[i] >= 1 and radii[i] <= 5:
        c+=1
        a = np.append(a, radii[i])

print(a)
print(c)

#print(np.count_nonzero(radii>1.4825 and radii < 1.5))

print(f"kleinstes Element in radii:{np.min(radii)}")


'''plt.hist(radii, bins=10, density=True, edgecolor='black')  # Bins einstellen
plt.xlabel('Porenradius (Pixel)')
plt.ylabel('Wahrscheinlichkeit')
plt.title('Histogramm der Porenradien (in Pixeln)')
plt.show()'''

# Plot 1: Graustufenbild
plt.subplot(1, 2, 1)
plt.imshow(grayscale_image, cmap='gray')
plt.title('Graustufenbild')
plt.axis('off')  # Achsen ausblenden

# Plot 2: Histogramm der Porengrößen
plt.subplot(1, 2, 2)
plt.hist(radii, bins=75, density=True, stacked=True, cumulative=True, rwidth = (1/75), edgecolor='black')  # Histogramm mit 10 Bins
plt.xlabel('Porenradius (Pixel)')
plt.ylabel('Wahrscheinlichkeit')
plt.title('Histogramm der Porenradien (in Pixeln)')

# Darstellung der Plots
plt.tight_layout()
plt.show()