#Write a pp to take 10-digit mobile number and display only the last 4 digits.Replace the first 6 digits with ******

number = input()
number1 = "******"+number[-4:]
print(number1)