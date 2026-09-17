#write a python program to print the inverted right - angled triangle using stars.
# * * * *
# * * *
# * * 
# * 

n = int(input("Enter the number : "))
for i in range(n):
  for j in range(n-i):
    print("*",end = " ")
  print()
