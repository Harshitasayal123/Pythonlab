#Write a Python program to input a number and check whether it is prime or not. A number is prime if it has no divisor other than 1 and itself.
number = int(input("Enter the number : "))
if number < 2:
  print("Number is not prime")
else:
  for i in range(2,number):
    if number%i==0:
      print("Number is not prime")
      break
  else:
    print("Number is prime")