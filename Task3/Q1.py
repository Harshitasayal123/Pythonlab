#Write a pp to take ttal minutes as input and convert it into hours and remaining minutes.
minutes = int(input())
hours = minutes//60
minutes = minutes%60
print(f"{hours}hrs and {minutes}mins")