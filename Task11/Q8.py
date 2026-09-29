#Write a pyhton program to count how many times a particular elements appears in a list.
number = [10,20,30,40,50,60,70]
search = int(input("Enter number to count: "))
count = 0

for num in number:
  if num == search:
    count = count+1

print("Frequency: ",count)