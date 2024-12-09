x =  []
y = []
y_raw = []
y_sum = 0


input_file = "..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_fiji_pore_size_distribution_roh.txt"
output_file = "..\\data\\pore_size_distribution\\Datensatz_PU-Schaum_30ppi_fiji_pore_size_distribution.txt"

#input_file = "..\\data\\strut_width_distribution\\Datensatz_PU-Schaum-30ppi_fiji_strut_wdith_distribution_roh.txt"
#output_file = "..\\data\\strut_width_distribution\\Datensatz_PU-Schaum-30ppi_fiji_strut_wdith_distribution.txt"



with open(input_file, "r") as file:
    for line in file:
        parts = line.strip().split(",")
        x.append(float(parts[1])) 
        y_raw.append(float(parts[2]))


for el in y_raw:
    y_sum = y_sum + el

n = 0

for el in y_raw:
    y.append((y_raw[n]/y_sum)*100)
    n += 1



c = 0

with open(output_file, "w") as file:
    for el in x:
        file.write(str(x[c])+"\t"+str(y[c])+"\n")
        c += 1

print(x)
print(y)