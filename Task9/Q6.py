#write a python program to input four number form the user and find the greatest number among them.
a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))
d = int(input("Enter fouth number : "))

if a>=b and a>=c and a>=d:
  print("Gretest number is : ",a)
elif b>=a and b>=c and b>=d:
  print("Gretest number is : ",b)
elif c>=b and c>=a and c>=d:
  print("Gretest number is : ",c)
else:
  print("Gretest number is : ",d)