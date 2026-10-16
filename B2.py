# Resistors in Series

num_resistors = int(input("How many resistors? "))
total_resistance = 0

for i in range(1, num_resistors + 1):
    resistance_val = float(input("Enter R" + str(i) + ": "))
    total_resistance += resistance_val

print("Total resistance =", total_resistance, "ohm")
