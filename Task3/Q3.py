#write a pp to take an amount in rupees and calculate how many rs 500 and rs 100 notes are needed
money = int(input())

n500 = money//500
remain = money%500

n100 = remain//100

print(f"{n500} 500 notes and {n100} 100 notes")
