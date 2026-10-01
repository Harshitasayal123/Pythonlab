#Write a program to perform searching activity using linear and binary search
list = list(map(int,input("Enter the list elements : ").split()))

target = int(input("Enter the element to search in list : "))
n = len(list)
position = -1
for i in range(n):
  if target==list[i]:
    position = i
    break
if position != 1:
  print("Element not found!")
else:
  print("The element found ")

sorted_list = sorted(list)
left_ind = 0
right_ind = n-1
position = -1

while left_ind <= right_ind:
  mid = (left_ind+right_ind)//2


  if sorted_list[mid] == target:
    position = mid
    break
  elif sorted_list[mid] > target:
    right_ind = mid-1
  else:
    left_ind = mid+1
if position != 1:
  print("Element not found!")
else:
  print("The element found ")






  