print("Hello world")
#Modules is file conataining code weitten by somebody else which can be imported and used in our program.

#pip is the package manager for python . You can use pip to install modules on your system.

# Types of modules:
# Built in modules: These are the modules which are already present in python. You can use them directly without installing them.Example: math, random, os, sys etc.
# External modules : These are the modules which are not present in python. You can install them using pip.


# Types of commnet in python :

#single line comment
#python is a case sensitive language
#multi line comment using double quotes
"""multi line comment 
using double quotes"""

#Write a python program which prints the conetents of the directory using os module .Search online for the function does that.
# import os
# print(os.listdir())

# directory = r"C:\Users\DELL\OneDrive\Desktop\fastapi-day1"
# for i in os.listdir(directory):
#     print(i)
# print(os.path.exists("practice1.py"))
# import os
# os.rmdir(r"C:\Users\DELL\OneDrive\Desktop\Python-lab\sample3")
# import os
# os.rmdir("sample3")


# import os

# folder = r"C:\Users\DELL\OneDrive\Desktop\Python-lab\sample3"

# if os.path.isdir(folder) and not os.listdir(folder):
#     os.rmdir(folder)
# else:
#     print("Folder is not empty or not found")
import os
os.rmdir("hhh")