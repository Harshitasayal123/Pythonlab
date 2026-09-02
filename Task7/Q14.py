#take an email address and check whehther it contain @ and .com

email = input("Enter the email address : ")
print(email.find('@')!=-1 and email.find('.com')!= -1)