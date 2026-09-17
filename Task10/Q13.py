#write a program to print floyd's triangle
# 1
# 2 3
# 4 5 6
# 7 8 9 10

n = int(input("Enter the number : "))
for i in range(n):
  for j in range(i,j):
    print(j,end = " ")
  print()