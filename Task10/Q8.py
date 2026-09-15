#Write a python program to repeadly calculate the sum of digits of a number until the result become a single digit
#Eg :- 9875 ->9+8+7+5 = 29 ->2 +9 = 11 -> 1+1 = 2
num = int(input("Enter the number: "))
while num>=10:
  sum_digit = 0

  while num>0:
    digit = num %10
    sum_digit = sum_digit +digit
    num = num//10

  num = sum_digit

print("Single digit result : ", num)