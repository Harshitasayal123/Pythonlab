# Write a Python program to check whether a given value is present in a tuple.
# If present, display its position.

n = tuple(map(int, input("Enter the tuple: ").split()))
num = int(input("Enter the number to find: "))

found = False

for i, value in enumerate(n):
    if num == value:
        print(f"The element is present at position {i}")
        found = True
        break

if not found:
    print("Element not found!!!!!!!!!")