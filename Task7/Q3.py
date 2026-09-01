#Write a pp to take an email address and print the domain name
email = input("Enter your email : ")

ind = email.find("@")
print(email[ind+1:])
