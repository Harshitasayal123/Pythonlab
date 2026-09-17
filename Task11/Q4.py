# write a python program to input a list of numbers and create new list conataining only unique elements.
number = []
unique_num = []

n = int(input("Enter total number: "))

for i in range(n):
  num = int(input("Enter number : "))
  number.append(num)

for num in number:
  if num not in unique_num:
    unique_num.append(num)

print("Original list: ", number)
print("Unique list:", unique_num)
