from analysis import calculate_porosity, calculate_pore_size_distribution, calculate_strut_width_distribution

def main():

    # dataset_path = "V:\\Horn, Thassilo\\BA\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted" # Uni
    dataset_path = "C:\\Users\\thass\\Desktop\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted" # Privat

    # Porosität berechnen
    porosity = calculate_porosity(dataset_path)
    print(porosity)

    # Porengrößenverteilung berechnen
    calculate_pore_size_distribution(dataset_path)

    # Stegbreitenverteilung berechnen
    calculate_strut_width_distribution(dataset_path)

    return 0

if __name__ == "__main__":
    main()