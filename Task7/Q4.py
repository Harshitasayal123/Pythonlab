#Write a pp to check wheather an email ends with mietjammu.in
email = input("Enter your email : ")
# ind = email.find("@")
# print(email[ind+1:] == "mietjammu.in")
print(email.endswith("mietjammu.in"))