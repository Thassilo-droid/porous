from utils import image_loader
import porespy as ps
import numpy as np

def calculate_pore_size_distribution(dataset_path):

    # Bilder zu 3 dimensionalem array zusammenfassen
    image_stack = image_loader.load_image_to_array(dataset_path)

    # Array im mit Porenradius berechnet durch local_thickness Funktion aus PoreSpy
    im = ps.filters.local_thickness(image_stack)

    # Alle Werte in ein 1 dimensionales array radii laden
    radii = im[im > 0].flatten()

    # Sortieren and Zählen der Werte aus radii array
    unique_values, counts = np.unique(radii, return_counts = True)

    # Anteil der einzelnen Werte aus radii berechnen
    total_count = len(radii)
    relative_frequencies = counts / total_count

    # Ergebnisse in Listen speichern
    pore_diameter = (unique_values*2).tolist()
    percentage = (relative_frequencies*100).tolist()

    # Porendurchmesser und prozentualer Anteil als Rückgabewert setzen
    return pore_diameter, percentage
