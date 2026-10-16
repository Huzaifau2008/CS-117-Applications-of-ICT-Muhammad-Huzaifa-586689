# Fuse Check (Ohm's Law)

voltage = float(input("Enter voltage = "))
resistance = float(input("Enter resistance= "))

if (resistance <= 0):
    print("Invalid resistance")
else:
    current = voltage / resistance
    print("Current =", current, "A")
    if (current > 2):
        print("Fuse will blow")
    else:
        print("Circuit is safe")
