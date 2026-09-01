#write a python program to fill the given letter template with name and data
# name = input("Enter the name : ")
# date = input("Enter the date : ")

# print(f"""Dear {name},
# You are selected
# {date}""")

letter = """
Dear <name>
You are selected!
<date>
"""
name = input("Enter the name : ")
date = input("Enter the date : ")

letter = letter.replace("<name>",name)
letter = letter.replace("<date>",date)
print(letter)