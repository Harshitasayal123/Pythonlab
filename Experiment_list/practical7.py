#Write a python program to create records of n students. Store each student record as a dictionary containing roll number, name branch, and marks. Store all records in a list and search for s student using roll number.(Condition: Roll numbers nust be unique)# Program to create and search student records

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    print("Enter details of student", i + 1)

    roll = int(input("Enter roll number: "))

    while any(student["roll"] == roll for student in students):
        print("Roll number already exists. Enter a unique roll number.")
        roll = int(input("Enter roll number: "))

    name = input("Enter name: ")
    branch = input("Enter branch: ")
    marks = float(input("Enter marks: "))

    student = {
        "roll": roll,
        "name": name,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

print("Student Records:")
for student in students:
    print(student)


search_roll = int(input("Enter roll number to search: "))

found = False

for student in students:
    if student["roll"] == search_roll:
        print("\nStudent found:")
        print("Roll Number:", student["roll"])
        print("Name:", student["name"])
        print("Branch:", student["branch"])
        print("Marks:", student["marks"])
        found = True
        break

if not found:
    print("Student with roll number", search_roll, "not found.")  