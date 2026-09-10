# Temperature conversion program

temp = float(input("Enter temperature: "))
choice = input("Convert to (C)elsius or (F)ahrenheit: ")

if choice.upper() == "F":
    # Celsius to Fahrenheit
    fahrenheit = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)

elif choice.upper() == "C":
    # Fahrenheit to Celsius
    celsius = (temp - 32) * 5/9
    print("Temperature in Celsius:", celsius)

else:
    print("Invalid choice")