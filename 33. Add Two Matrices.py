#Add Two Matrices 

r = int(input("Rows: "))
c = int(input("Columns: "))

A = [[int(input()) for j in range(c)] for i in range(r)]
B = [[int(input()) for j in range(c)] for i in range(r)]

print("Result Matrix:")
for i in range(r):
    for j in range(c):
        print(A[i][j] + B[i][j], end=" ")
    print()
