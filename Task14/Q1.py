# create a class and object : student details
#Problem: Create a Student class to store a student's name and roll number.
#Create an object and display the details using an instance method


class Student:
  def __init__(self,name, roll_no):
    self.name = name
    self.roll_no = roll_no
  def display(self):
    print(self.name)
    print(self.roll_no)

student1 = Student("Anuj",21)
student1.display()