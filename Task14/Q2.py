#Instance method: rectangle area and perimeter
#Problem: Create a Rectangle class with length and beeadth.Use instance
#methods to calculate its area and perimeter

class Rectangle:
  def __init__(self,length,breadth):
    self.length = length
    self.breadth = breadth

  
  def area(self):
    print("Area of rectangle: ",self.length*self.breadth)
  def perimeter(self):
    print("Perimeter of rectangle: ",2*(self.length+self.breadth))
length= int(input("Enter the length: "))
breadth= int(input("Enter the breadth: "))
rectangle1 = Rectangle(length,breadth)
rectangle1.area()
rectangle1.perimeter()
  