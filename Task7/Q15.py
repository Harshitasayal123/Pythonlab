#Take a sentence conatining double spaces and unwanted spaces at the beginning or end . Clean the sentence
sentence = input("Enter the sentence : ").strip()

snetence = sentence.replace("  "," ")
print(sentence)