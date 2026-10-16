# Resistor Colour Code

x= input("Enter band colour: ").lower()

colours = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
}

if ( x in colours):
    print("Digit =",colours[x])
else:
    print("Invalid colour")
