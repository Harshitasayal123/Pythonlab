#Write a pyhton program to show that tuple value cannot be chnaged directly . Convert tuple into list, update it and convert it back into tuple.
tuple1 = (1,2,3,4,5)
#tuple[3]=9
print("Original tuple:",tuple1)

list1 = list(tuple1)
list1[3]=9
tuple1 = tuple(list1)
print("after updation new tuple is : ", tuple1)