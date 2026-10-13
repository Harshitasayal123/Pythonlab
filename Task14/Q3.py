#Create a Product class with product name , price and quantity . Add an instance method to calculate the total cost. Take these 
# values from the user and display the product name and total cost


class Product:
  def __init__(self,name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def total_cost(self):
    print("Total_cost : ",self.price*self.quantity)
name = input("Enter the name of the product: ")
price = int(input("Enter the price of the product: "))
quantity = int(input("Enter the quantity of the product: "))

Product1 = Product(name, price, quantity)
Product1.total_cost()