#Write a pp to input marks of 5 students
#FOR each studnet , the program should check whether the enterd marks are valid or nvalid. Marks
#are considered valid only if they are between 0a and 100. If the marks are invalid, the program should
#display "invlaid marks skipped" and move to the enxt studnet without printing those marks.
#if the marks are valid , the program should display the marks as valis.

for i in range(1,6):
  marks = int(input("Enter marks for students : "))
  if marks>0 and marks<100:
    print("valid marks for student")
  else:
    print("Invalid marks skipped for students ")
