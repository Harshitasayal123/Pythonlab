#Write a python program to store all month name in tuple . Input a month number and display the corresponding month name
Months = ("January","Februray","March","April","May","June","July","August","September","October","November","December")
m = int(input("Enter month number: "))
print(f"{m}th mpnth of the year is {Months[m-1]}" )