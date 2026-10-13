#Create a BankAccount class that stores an account holder's name and balance .Add instance methods to deposit money ,
#  withdraw money, and display the balance.Do Not allow a withdrawl greater than available balance


class BankAccount:
  def ___init__(self,name, balance):
    self.name = name
    self.balance = balance

  def deposit(self,money):
    return self.balance+money
  def withdrwal(self,money):
    if money>self.balance:
      print("Insufficient balance")
    else:
      return self.balance-money
  def display(self):
    print("Total balance is : ",self.balance)
name = input("Enter the account holder name: ")
balance = int(input("Enter the balance: "))
Account1 = BankAccount(name,balance)
Account1.deposit(2000)
Account1.withdrwal(3000)
Account1.display()



  