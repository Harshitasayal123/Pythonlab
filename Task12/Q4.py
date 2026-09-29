#Write a python program to store repeated values in a tuple and count how many times a given value appear
tuple1 = tuple(map(int,input("Enter the tuple list : ").split()))
num = int(input("Enter the number : "))
count = tuple1.count(num)
print("Tuple is : ",tuple1)
print(f"The {num} value appears {count} in the tuple list")