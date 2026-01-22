# Largest Number Among Three

A = int (input("Enter value of A: "))
B = int (input("Enter value of B: "))
C = int (input("Enter value of C: "))

if A>B and A>C:
    print("A is greater =", A)
elif B>A and B>C:
    print("B is greater =", B)
else:
    print("C is greater =", C)