#Take name , branch and year. Generate a code name using string concatenation, slicing and repetition.
name = input()
branch = input()
year = int(input())

code = name[:3] + "-" + branch[:3] + "-" + year[-2:]

print("*" * 30)   
print("Student Code : ",name)
print("*" * 30)