#write a python program to rotate a list one postition to the right

rot = []
n = int(input("Enter total number : "))

for i in range(n):
  num = int(input("Enter the number: "))
  rot.append(num)
last = rot.pop()
rot.insert(0,last)

print("New list: ",rot)