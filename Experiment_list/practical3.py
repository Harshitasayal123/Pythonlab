# Given string
text = "Welcome to Python world"

# 1. Count the number of alphabets
count = 0
for char in text:
    if char.isalpha():
        count += 1

print("Number of alphabets:", count)

# 2. Extract characters from a given range
# Example: extracting characters from index 0 to 6
print("Extracted characters:", text[0:7])

# 3. Check whether the string is alphanumeric
if text.isalnum():
    print("The string is alphanumeric")
else:
    print("The string is not alphanumeric")