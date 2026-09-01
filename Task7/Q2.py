# Write a pp to take a student and roll number , then generate a username using the first 3 letter of the name and last 2 digits of the roll number

name = input("Enter your name : ")
rollno = input("ENter your rollno : ")

username = name[0:3:1] +rollno[-2:]
print(username)
#+rollno[-2,-1]