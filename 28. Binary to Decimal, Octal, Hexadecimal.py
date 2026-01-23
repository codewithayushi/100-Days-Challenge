# Binary to Decimal, Octal, Hexadecimal

binary = input("Enter binary number: ")

# Binary to Decimal
decimal = int(binary, 2)
print("Decimal:", decimal)

# Binary to Octal
print("Octal:", oct(decimal)[2:])

# Binary to Hexadecimal
print("Hexadecimal:", hex(decimal)[2:].upper())


