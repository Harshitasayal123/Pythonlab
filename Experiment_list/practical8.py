# create a database using list and tuples. Each student record must contain roll number, name, branch and CGPA. Store all record as tuple inside a list. Display all records and 
# search for a students using roll number.
#Condition
#Each record should ne stored in tuple.
#The complete database should be stored as a list
#Roll number must be unique.


database = []
n = int(input("Enter the number of students: "))
for i in range(n):
  roll_no = input("Enter the roll number: ")
  name = input("Enter the name: ")
  branch = input("Enter the branch: ")
  cgpa = float(input("Enter the cgpa: "))
  student_record = (roll_no,name,branch,cgpa)
  database.append(student_record)
print("\nStudent database")
for student in database:
  print(student)
search_roll = input("Enter the roll number to search:")
found = False

for studnet in database:
  if student[0] == search_roll:
    print("Student Record Found")
    print("Roll number:",studnet[0])
    print("Name: ",student[1])
    print("branch: ",student[2])
    print("Cgpa: ",student[3])
    found = True
    break

if found == False:
  print("studnet not found")
