#Write a python program  to input a students marks in n consecutive tests and store them in a list. Find the longest consecutive sequence in which each marks is strictly greater than the previous mark.
#Display the sequeence its length, its starting and ending test numbers as tuple. If multiple sequence have the same maximum length, display the first one.
#Marks :[55,60,68,62,65,70,78,74]
#Longest improving sequence: [62,65,70,78]
#Number of test: 4
#test range:[4,7]
#Conditions:
#Accept at least one test
#Equal marks break the improving sequence
#Test number begin at 1
#Do not sort the list because the original test order matters.
n = int(input("enter the number of subjects: "))
marks = list(map(int,input("Enter the marks of n subjects: ").split()))
