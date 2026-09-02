# write a python program to take a string and seperate charcters present at even index positions and odd index position
string = input("Enter the string : ")
length = len(string)
even = string[0:length:2]
odd = string[1:length:2]
print(odd)
print(even)