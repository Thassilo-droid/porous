
x = []
y = []

# \\..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_CTan_pore_size_distribution.txt

with open("..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_CTan_pore_size_distribution_roh.txt", "r") as file:
    for line in file:
        # Split the line by ',' to extract values
        parts = line.strip().split(",")
        # Add the second value to x and the fourth value to y
        x.append(float(parts[1]))
        y.append(float(parts[3]))

c = 0

with open("..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_CTan_pore_size_distribution.txt", "w") as file:
    for el in x:
        file.write(str(x[c])+"\t"+str(y[c])+"\n")
        c += 1



print(x)
print(y)
