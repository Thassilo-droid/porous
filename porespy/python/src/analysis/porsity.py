from utils import image_loader
import porespy as ps

def calculate_porosity(dataset_path):

    # Bilder zu 3 dimensionalem array zusammenfassen
    image_stack = image_loader.load_image_to_array(dataset_path)

    # Porosität mit PoreSpy Funktione berechnen lassen
    porosity = ps.metrics.porosity(image_stack)

    # Porosität als Rückgabewert setzen
    return porosity