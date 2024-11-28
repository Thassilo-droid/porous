import matplotlib.pyplot as plt

# inverted: void: white (True); solid: black (False) 
#   -> trabecular thickness (Tb,Th): Poresize;
#   -> trabecular separation (Tb,Sp): Strut width;

# non_inverted: void: black (False); solid: white (True)
#   -> trabecular thickness (Tb,Th): Strut width;
#   -> trabecular separation (Tb,Sp): Poresize;

# inverted:

x_inverted_TbTh = []
y_inverted_TbTh = []

x_err_inverted = 30.45458003 # standard deviation (in pixels)

# Open and read the file line by line
with open("inverted_TbTh.txt", "r") as file:
    for line in file:
        # Split the line by ',' to extract the values
        parts = line.strip().split(",")
        # Add the second value to x and the fourth value to y
        x_inverted_TbTh.append(float(parts[1]))
        y_inverted_TbTh.append(float(parts[3]))


# non_inverted:

x_non_inverted_TbTh = []
y_non_inverted_TbTh = []

x_err_non_inverted = 2.97785434 # standard deviation (in pixels)

# Open and read the file line by line
with open("non_inverted_TbTh.txt", "r") as file:
    for line in file:
        # SPlit the line by ',' to extract the values
        parts = line.strip().split(",")
        # Add the second value to x and the fourth value to y
        x_non_inverted_TbTh.append(float(parts[1]))
        y_non_inverted_TbTh.append(float(parts[3]))


# Plotting (inverted)
plt.figure(figsize=(10, 6))  # Set the figure size
#plt.plot(x_inverted_TbTh, y_inverted_TbTh, marker='o', linestyle='-', color='b', label="Data Points")  # Line plot with markers
plt.errorbar(
    x_inverted_TbTh, y_inverted_TbTh, 
    xerr=x_err_inverted, fmt='o', linestyle='-', color='b', label="Data Points"
)  # Plot with x-error bars
plt.title("Plot of Extracted Data", fontsize=14)  # Add title
plt.xlabel("Mid-range [pixel]", fontsize=12)  # X-axis label
plt.ylabel("Percent Volume in range [%]", fontsize=12)  # Y-axis label
plt.grid(True)  # Add grid
plt.legend()  # Add legend
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot


'''
# Plotting (non_inverted)
plt.figure(figsize=(10, 6)) # Set the figure size
#plt.plot(x_non_inverted_TbTh, y_non_inverted_TbTh, marker='o', linestyle='-', color='b', label="Data Points")  # Line plot with markers
plt.errorbar(
    x_non_inverted_TbTh, y_non_inverted_TbTh, 
    xerr=x_err_non_inverted, fmt='o', linestyle='-', color='b', label="Data Points"
)  # Plot with x-error bars
plt.title("Plot of Extracted Data", fontsize=14)  # Add title
plt.xlabel("Mid-range [pixel]", fontsize=12)  # X-axis label
plt.ylabel("Percent Volume in range [%]", fontsize=12)  # Y-axis label
plt.grid(True)  # Add grid
plt.legend()  # Add legend
plt.tight_layout()  # Adjust layout
plt.show()  # Display the plot)
'''