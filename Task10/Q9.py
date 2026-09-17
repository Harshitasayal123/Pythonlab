# Write a pyhton program to print the following pattern for n rows:
# 1
# 1 2
# 1 2 3
# 1 2 3 4

num = int(input("Enter the number: "))
for i in range(1,num+1):
  for j in range(1,i+1):
    print(j,end= " ")

  print()