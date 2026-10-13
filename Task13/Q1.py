# Create a class and object: student details
#Problem: Create 


# class Student:
#   def __init__(self,name,roll_number):
#     self.name = name
#     self.roll_number = roll_number

#   def display_details(self):
#     print("Name: ",self.name)
#     print("Roll Number : ", self.roll_number)

# student1 = Student("Aman",25)
# student1.display_details()


#class Student defines a class
# student1 is an object of the student
# class__init__() assigns value when the object is created
# self refer to the object being used
# display_details() us an instance method because it works with an object's data


class Train:
  def __init__(self,number_of_seats,fare):
    self.number_of_seats = number_of_seats
    self.fare = fare

  def book(self,tickets=1):
    self.number_of_seats -= tickets
    if number_of_seats<0:
      self.number_of_seats += tickets
      print("Seats are not available")

      