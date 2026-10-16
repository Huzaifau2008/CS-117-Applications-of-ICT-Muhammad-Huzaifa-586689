# Current and Power[cite: 5]

def ohms_current(v,r):
    return v/r

def power_dissipated(i, r):
    return (i**2)*r

voltage_val=12
resistance_val=6

current_result=ohms_current(voltage_val, resistance_val)
power_result=power_dissipated(current_result, resistance_val)

print("Current =",current_result,"A")
print("Power =",power_result,"W")
