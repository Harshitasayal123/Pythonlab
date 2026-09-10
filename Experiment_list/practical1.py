
# Program to demonstrate type checking and built-in functions

# Different data types
a = 25
b = 12.5
c = "Python"
d = True
e = [10, 20, 30, 40]
f = (5, 10, 15)

# Type checking using type()
print("Data Types:")
print("a =", a, "Type:", type(a))
print("b =", b, "Type:", type(b))
print("c =", c, "Type:", type(c))
print("d =", d, "Type:", type(d))
print("e =", e, "Type:", type(e))
print("f =", f, "Type:", type(f))

# abs() - returns the absolute value
num = -25
print("\nAbsolute value of", num, "=", abs(num))

# len() - returns the number of elements/characters
word = "Python"
print("Length of", word, "=", len(word))

# min() - returns the smallest value
numbers = [10, 5, 25, 3, 15]
print("Minimum value =", min(numbers))

# round() - rounds a number
decimal_num = 15.6789
print("Rounded value =", round(decimal_num, 2))

# isalnum() - checks whether all characters are alphanumeric
text1 = "Python123"
text2 = "Python 123"   

print(text1, "is alphanumeric:", text1.isalnum())
print(text2, "is alphanumeric:", text2.isalnum())



