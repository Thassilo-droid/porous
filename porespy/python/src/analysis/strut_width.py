from utils import image_loader
import porespy as ps
import numpy as np
import os

def calculate_strut_width_distribution(dataset_path):

    # Bilder zu 3 dimensionalem array zusammenfassen/ invertieren, damit Porengröße am Feststoff gemessen wird (Stegbreite)
    image_stack = image_loader.load_image_to_array(dataset_path, inverter = True)

    # Array mit Porenradius berechnet durch local_thickness Funktion aus PoreSpy
    im = ps.filters.local_thickness(image_stack)

    # Alle Werte in ein 1 dimensionales array radii laden
    radii = im[im > 0].flatten()
    
    # Sortieren und Zählen der Werte aus radii array
    unique_values, counts = np.unique(radii, return_counts = True)

    # Anteil der einzelnen Werte aus radii berechnen
    total_count = len(radii)
    relative_frequencies = counts / total_count

    # Ergebnisse in Listen speichern
    strut_diameter = (unique_values*2).tolist() # Porendurchmesser = 2 * Porenradius
    percentage = (relative_frequencies*100).tolist() # Prozentsatz berechnen

    # Dateinamen aus dataset_path generieren
    path_parts = os.path.normpath(dataset_path).split(os.sep)  # Pfadteile extrahieren
    if len(path_parts) >= 2:
        dataset_name = f"{path_parts[-2]}_{path_parts[-1]}"  # Vorletzter und letzter Teil kombinieren
    else:
        dataset_name = path_parts[-1]  # Fallback, falls Pfad kürzer ist
    file_name = f"{dataset_name}_strut_width_distribution.txt"  # Dynamischer Dateiname

    # Pfad zu output_data (relativ zur Projektstruktur)
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    output_dir = os.path.join(project_root, "output_data")
    os.makedirs(output_dir, exist_ok=True)  # Ordner erstellen, falls er nicht existiert
    output_file = os.path.join(output_dir, file_name)

    # Ergebnisse in Datei schreiben
    with open(output_file, "w") as f:
        f.write("Strut Width (pixels)\tPercentage (%)\n")
        f.write("--------------------------------------\n")
        for diameter, probability in zip(strut_diameter, percentage):
            f.write(f"{diameter}\t{probability:.2f}\n")

    # Rückgabewert: Pfad zur gespeicherten Datei
    return output_file