from analysis import calculate_porosity, calculate_pore_size_distribution, calculate_strut_width_distribution

def main():

    porosity = calculate_porosity("V:\\Horn, Thassilo\\BA\\Daten\\Datensatz_PU-Schaum_30ppi\\non_inverted")

    print(porosity)

    return 0

if __name__ == "__main__":
    main()