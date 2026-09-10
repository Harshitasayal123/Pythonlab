#Write a python program to input number reverse it using arithmetic operations only.
num = int(input("Enter the number : "))
new_num = 0
while num!=0:
  remainder = num%10
  num = num//10
  new_num = new_num*10+remainder

print(new_num)