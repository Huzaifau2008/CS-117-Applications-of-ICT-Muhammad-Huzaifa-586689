# Resistor Tolerance Sorting

count_1_percent = 0
count_5_percent = 0
count_reject = 0

while (True):
    measured_resistance = float(input("Enter measured resistance (0 to stop): "))
    if (measured_resistance == 0):
        break
    
    if (99.0 <= measured_resistance <= 101.0):
        count_1_percent += 1
    elif (95.0 <= measured_resistance <= 105.0):
        count_5_percent += 1
    else:
        count_reject += 1

print("1% tolerance resistors:", count_1_percent)
print("5% tolerance resistors:", count_5_percent)
print("Rejected resistors:", count_reject)
