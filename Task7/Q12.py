# write a python program to take a password and check whether it conatins @ and has at least 8 charcters.
password = input("Enter the password : ")
print(password.find('@')!=-1 and len(password)>=8)