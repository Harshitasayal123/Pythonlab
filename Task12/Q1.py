#Write a pyhton program to store two points as a tuple and calculate the distance bwetween them
import math
x1 = float(input("Enter x1 : "))
y1 = float(input("Enter y1 : "))
x2 = float(input("Enter x2 : "))

y2 = float(input("Enter y2 : "))

point1 = (x1,y1)
point2 = (x2,y2)

distance = math.sqrt(((point2[0]-point1[0])**2) +((point2[1]-point1[1])**2))
print("point1: ",point1)
print("point2: ",point2)
print("Total distance : ", distance)
