import random
letters="ABCDEFabcdef"
numbers="1234567890"
all_symbols= letters + numbers
length=int(input("какой длинны нужен пороль? "))
password= ""
for i in range (length):
    password+=random.choice(all_symbols)
print(password)
