#Write a python program to input a decimal and convert it into binary without using the built-in bin() funaction
number = int(input("Enter the decimal number: "))

new_number = 0
place = 1

while number != 0:
    remainder = number % 2
    number = number // 2

    new_number = new_number + remainder * place
    place = place * 10

print("Binary conversion:", new_number)