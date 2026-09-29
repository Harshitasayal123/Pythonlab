#Write a pyhton program to store multiple studnets records as a list of tuples. Each tuple should contain name, roll number, and marks. Display students who scored above 75.
n = int(input("Enter the number of students: "))

students = []

for i in range(n):
    name = input("Enter student name: ")
    roll = int(input("Enter roll number: "))
    marks = int(input("Enter marks: "))

    students.append((name, roll, marks))

print("\nStudents who scored above 75:")

for student in students:
    if student[2] > 75:
        print(student)