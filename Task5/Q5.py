#Write a pp to take studnet details like name, roll , number , CGPA and hostel status from the user . TYpecast them into appropriate types and print them along with their detected type
name = input()
roll_number = int(input())
Cgpa = int(input())
status = input()

print(name, type(name))
print(roll_number, type(roll_number))
print(Cgpa, type(Cgpa))
print(status, type(status))