#write a pp to take words and count the number of vowels a, e, i, o and u.
word = input("Enter the word : ")
vowels = 'aeiouAEIOU'
count = 0
for char in word:
    if char in vowels:
        count += 1
print("Number of vowels in the word:", count)

