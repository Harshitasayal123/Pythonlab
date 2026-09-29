#Write a pyhton program where the user can add items, remove items , view cart, and exit
cart = []
while True:
  print("1.Add Item")
  print("2.Remove item")
  print("3.View cart")
  print("4.Exit")

  choice = int(input("Enter choice: "))
  if choice== 1:
    item = input("Enter item name: ")
    cart.append(item)

  elif choice ==2:
    item = input("Enter item to remove: ")
    if item in cart:
      item.remove()
  elif choice ==3:
    for item in cart:
      print("list: ", item)
  elif choice == 4:
    exit()

  else:
    print("Invalid choice")