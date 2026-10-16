# Current and Power[cite: 5]

def ohms_current(v,r):
    return v/r

def power_dissipated(i, r):
    return (i**2)*r

voltage=12
resistance=6

current_result=ohms_current(voltage, resistance)
power_result=power_dissipated(current_result, resistance)

print("Current =",current_result,"A")
print("Power =",power_result,"W")
