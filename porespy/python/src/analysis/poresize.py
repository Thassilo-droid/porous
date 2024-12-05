from utils import image_loader
import porespy as ps
import numpy as np
import os

def calculate_pore_size_distribution(dataset_path):

    # Bilder zu 3 dimensionalem array zusammenfassen
    image_stack = image_loader.load_image_to_array(dataset_path)

    # Array mit Porenradius berechnet durch local_thickness Funktion aus PoreSpy
    im = ps.filters.local_thickness(image_stack)

    # Alle Werte in ein 1 dimensionales array radii laden
    radii = im[im > 0].flatten()

    # Sortieren and Zählen der Werte aus radii array
    unique_values, counts = np.unique(radii, return_counts = True)

    # Anteil der einzelnen Werte aus radii berechnen
    total_count = len(radii)
    relative_frequencies = counts / total_count

    # Ergebnisse in Listen speichern
    pore_diameter = (unique_values*2).tolist() # Porendurchmesser = 2 * Porenradius
    percentage = (relative_frequencies*100).tolist() # Prozentsatz berechnen
    
    # Pfad zur Ausgabedatei
    output_file = os.path.join("..\\..\\..\\output_data", "pore_size_distribution.txt")

    # Ergebnisse in Datei schreiben
    with open(output_file, "w") as f:
        f.write("Pore Diameter (pixels)\tPercentage (%)\n")
        f.write("--------------------------------------\n")
        for diameter, probability in zip(pore_diameter, percentage):
            f.write(f"{diameter}\t{percentage:.2f}\n")



    # Porendurchmesser und prozentualer Anteil als Rückgabewert setzen
    #return pore_diameter, percentage

    # output_file als Rückgabewert setzen
    return output_file