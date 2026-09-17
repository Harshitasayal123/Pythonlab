#write a python program to print the right - angled triangle using stars.
# *
# * *
# * * *
# * * * *

n = int(input("Enter the number : "))
for i in range(1,n+1):
  for j in range(1,i+1):
    print("*",end = " ")
  print()
