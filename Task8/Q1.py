#take a student full name and roll number. Gneerate emial using first 3 letters of the first name, first 3 letter of last name, and last 3 characters of roll number.
name = input("Enter you name : ")
rollno = input("Enter you rollno : ")
space_index = name.find(" ")

first_name =name[:space_index]
last_name = name[space_index]