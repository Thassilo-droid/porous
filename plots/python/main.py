import matplotlib.pyplot as plt
import numpy as np

degree = 12

# CTan

x_poresize_ctan = []
y_poresize_ctan = []
input_poresize_ctan = "..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_CTan_pore_size_distribution.txt"
with open(input_poresize_ctan, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_poresize_ctan.append(float(parts[0]))
        y_poresize_ctan.append(float(parts[1]))

# Polynom
p_poresize_ctan = np.polyfit(x_poresize_ctan, y_poresize_ctan, degree)

# Gute x-Werte und y-Werte um das Polynom zu fitten
x_poresize_ctan_fit = np.linspace(min(x_poresize_ctan), max(x_poresize_ctan), 100)
y_poresize_ctan_fit = np.polyval(p_poresize_ctan, x_poresize_ctan_fit)


x_strutwidth_ctan = []
y_strutwidth_ctan = []
input_strutwidth_ctan = "..\\data\\strut_width_distribution\\Datensatz_PU-Schaum-30ppi_CTan_strut_wdith_distribution.txt"
with open(input_strutwidth_ctan, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_strutwidth_ctan.append(float(parts[0]))
        y_strutwidth_ctan.append(float(parts[1]))

# Polynom
p_strutwidth_ctan = np.polyfit(x_strutwidth_ctan, y_strutwidth_ctan, degree)

# Gute x-Werte und y-Werte um das Polynom zu fitten
x_strutwidth_ctan_fit = np.linspace(min(x_strutwidth_ctan), max(x_strutwidth_ctan), 100)
y_strutwidth_ctan_fit = np.polyval(p_strutwidth_ctan, x_strutwidth_ctan_fit)

# Fiji

x_poresize_fiji = []
y_poresize_fiji = []
input_poresize_fiji = "..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_fiji_pore_size_distribution.txt"
with open(input_poresize_fiji, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_poresize_fiji.append(float(parts[0]))
        y_poresize_fiji.append(float(parts[1]))

# Polynom
p_poresize_fiji = np.polyfit(x_poresize_fiji, y_poresize_fiji, degree)
# Gute x-Werte und y-Werte um das Polynom zu fitten
x_poresize_fiji_fit = np.linspace(min(x_poresize_fiji), max(x_poresize_fiji), 100)
y_poresize_fiji_fit = np.polyval(p_poresize_fiji, x_poresize_fiji_fit)


x_strutwidth_fiji = []
y_strutwidth_fiji = []
input_strutwidth_fiji = "..\\data\\strut_width_distribution\\Datensatz_PU-Schaum-30ppi_fiji_strut_wdith_distribution.txt"
with open(input_strutwidth_fiji, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_strutwidth_fiji.append(float(parts[0]))
        y_strutwidth_fiji.append(float(parts[1]))

# Polynom
p_strutwidth_fiji = np.polyfit(x_strutwidth_fiji, y_strutwidth_fiji, degree)
# Gute x-Werte und y-Werte um das Polynom zu fitten
x_strutwidth_fiji_fit = np.linspace(min(x_strutwidth_fiji), max(x_strutwidth_fiji))
y_strutwidth_fiji_fit = np.polyval(p_strutwidth_fiji, x_strutwidth_fiji_fit)

# PoreSpy

x_poresize_porespy = []
y_poresize_porespy = []
input_poresize_porespy = "..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_PoreSpy_pore_size_distribution.txt"
with open(input_poresize_porespy, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_poresize_porespy.append(float(parts[0]))
        y_poresize_porespy.append(float(parts[1]))

# Polynom
p_poresize_porespy = np.polyfit(x_poresize_porespy, y_poresize_porespy, degree)
# Gute x-Werte und y-Werte um das Polynom zu fitten
x_poresize_porespy_fit = np.linspace(min(x_poresize_porespy), max(x_poresize_porespy), 100)
y_poresize_porespy_fit = np.polyval(p_poresize_porespy, x_poresize_porespy_fit)

x_strutwidth_porespy = []
y_strutwidth_porespy = []
input_strutwidth_porespy = "..\\data\\strut_width_distribution\\Datensatz_PU-Schaum-30ppi_PoreSpy_strut_wdith_distribution.txt"
with open(input_strutwidth_porespy, "r") as file:
    for line in file:
        parts = line.strip().split("\t")
        x_strutwidth_porespy.append(float(parts[0]))
        y_strutwidth_porespy.append(float(parts[1]))

# Polynom
p_strutwidth_porespy = np.polyfit(x_strutwidth_porespy, y_strutwidth_porespy, degree)
# Gute x-Werte und y-Werte um das Polynom zu fitten
x_strutwidth_porespy_fit = np.linspace(min(x_strutwidth_porespy), max(x_strutwidth_porespy), 100)
y_strutwidth_porespy_fit = np.polyval(p_strutwidth_porespy, x_strutwidth_porespy_fit)
    

# Plotte die Bar plots
plt.bar(x_poresize_ctan, y_poresize_ctan, color="blue", label="CTan")
plt.bar(x_poresize_fiji, y_poresize_fiji, color="orange", label="fiji")
plt.bar(x_poresize_porespy, y_poresize_porespy, color="green", label="PoreSpy")

# Plotte Polynome
plt.plot(x_poresize_ctan_fit, y_poresize_ctan_fit, color="blue")
plt.plot(x_poresize_fiji_fit, y_poresize_fiji_fit, color="orange")
plt.plot(x_poresize_porespy_fit, y_poresize_porespy_fit, color="green")

plt.title("Barplot of poresize", fontsize=20)
plt.xlabel("Pore Diameter [pixel]", fontsize=18)  # X-axis label
plt.ylabel("Percentage [%]", fontsize=18)  # Y-axis label
plt.grid(axis='y', linestyle='--')  # Horizontale Linien für bessere Lesbarkeit
plt.legend(fontsize = 18)  # Add legend
plt.tight_layout()  # Adjust layout
plt.show()