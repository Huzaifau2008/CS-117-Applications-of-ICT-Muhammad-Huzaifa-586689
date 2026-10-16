# Logic Gates

a = int(input("Enter A= "))
b = int(input("Enter B= "))

if ((a != 0 and a != 1) or (b != 0 and b != 1)):
    print("Bits must be 0 or 1")
else:
    and_output = 1 if (a == 1 and b == 1) else 0
    or_output = 1 if (a == 1 or b == 1) else 0
    xor_output = 1 if (a != b) else 0

    print("AND =", and_output)
    print("OR =", or_output)
    print("XOR =", xor_output)
