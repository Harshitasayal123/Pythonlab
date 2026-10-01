#write a python program to reverse every kth row in matrix.
# Reverse every K-th row in a matrix

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

matrix = []

print("Enter matrix elements:")
for i in range(r):
    row = list(map(int, input().split()))
    matrix.append(row)

k = int(input("Enter k: "))

# Reverse every k-th row
for i in range(k - 1, r, k):
    matrix[i].reverse()

print("Matrix after reversing every", k, "th row:")
for row in matrix:
    print(*row)