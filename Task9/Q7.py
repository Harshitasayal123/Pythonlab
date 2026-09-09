#Write a python program to detect whether a comment is span or not. A comment should be treated as spam if it contain any these keywords: "make a lot of money",
#"buy now", "subscribe this", or "click this"
comment = input("Enter the comment : ")
comment = comment.lower()
if "make a lot of money" in comment or "buy now"in comment or "subscribe this" in comment or "click this" in comment:
  print("SPAM !!!")
else:
  print("NO SPAM")