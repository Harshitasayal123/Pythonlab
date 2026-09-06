# take a password and check length, present of @ and whether first and last character are different
password = input("Enter your password : ")
# length = len(password)
# print("length : ",length)

# print(password.find('@') and password[0]==password[-1])

print("Length at least 8 : ", len(password)>= 8)
print("contains @ : ", "@ " in password)
print("First and last different ", password[0] != password[-1])