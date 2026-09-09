#Write a pyhton program that asks the user to enter the user name and password. The user should get only 3 attempts. If the correct credentials 
# are entered, display "login Successful" and stop the loop . If all attempt are used , display "Account Locked"
correct_username = "Harshita"
correct_password = "Harshita1234"
attempt = 3

while attempt >0:
  username = input("Enter username : ")
  password = input("Enter password : ")
  if username == correct_username and password == correct_password:
    print("Login successful")
    break
  else:
    attempt = attempt-1
    print("Wrong details. Attempt left: ", attempt)
if attempt == 0:
  print("Account Locked")


# for i in range(3):
#   username = input("Enter the username : ")
#   password = input("Enter the password : ")

#   if username != correct_username and password == correct_password:
#     print("Wrong username")
#   elif username == correct_username and password != correct_password:
#     print("Wrong password")
#   elif username != correct_username and password != correct_password:
#     print("Wrong username and password")
#   else:
#     print("login successfully")
#     break

# print("Locked")