#Create a BankAccount class that stores an account holder's name and balance .Add instance methods to deposit money ,
#  withdraw money, and display the balance.Do Not allow a withdrawl greater than available balance


class BankAccount:
  def __init__(self,name, balance):
    self.name = name
    self.balance = balance

  def deposit(self,money1):
    self.balance= self.balance+money1
  def withdrawl(self,money2):
    if money2>self.balance:
      print("Insufficient balance")
    else:
      self.balance= self.balance-money2
  def display(self):
    print("\nAccount Holder name : ",self.name)
    print("Total balance is : ",self.balance)
name = input("Enter the account holder name: ")
balance = int(input("Enter the balance: "))
money1 = int(input("Enter the money to deposit: "))
money2 = int(input("Enter the money to withdrawl: "))
Account1 = BankAccount(name,balance)
Account1.deposit(money1)
Account1.withdrawl(money2)
Account1.display()



  