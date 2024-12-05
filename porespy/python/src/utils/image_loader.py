import os
import numpy as np
from skimage.io import imread
from skimage.color import rgb2gray

def load_image_to_array(folder_path, inverter = False):

    # Sortierte List der .pngs aus dem Ordner
    file_list = sorted([f for f in os.listdir(folder_path) if f.endswith('.png')])

    # Bilder laden und Schwellenwert zur Binärisation setzen. In 3D numpy array laden
    images = []

    for file in file_list:

        # Bild laden
        image = imread(os.path.join(folder_path, file))

        # Konvertiere zu Graustufe um 4 Dimension aus array zu beseitigen
        if image.ndim == 3 and image.shape[-1] == 3:
            image = rgb2gray(image)

        # Schwellenwert setzen um Bild zu binärisieren
        if inverter == True:
            binary_image = image > 0.5 # Wahr und Falsch werden vertauscht. Schwarz wird Wahr und Weiß wird Falsch
        else:
            binary_image = image < 0.5 # Schwarz wird Falsch und Weiß wird Wahr

        # Binärisierte Bilder zu images[] Liste hinzufügen
        images.append(binary_image)

    return np.array(images)