#write a python program to input number in a list and create two sepreate list for even and odd number.

number = []
even = []
odd = []
n = int(input("Enter total elements: "))
for i in range(n):
  num = int(input("Enter the elements: "))
  number.append(num)

for num in number:
  if num%2==0:
    even.append(num)

for num in number:
  if num%2!=0:
    odd.append(num)   

print("Odd number list : ",odd)
print("Even number list : ",even)