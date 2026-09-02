# write a python program to take a word and print it in reverse order using slicing. Check whether it is the same forward and backward.
word = input("Enter the word: ")
reverse_word = word[::-1]
print(reverse_word)
print("Is the word the same forward and backward?", word == reverse_word)