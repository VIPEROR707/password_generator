import random
import string

letters=string.ascii_letters
numbers=string.digits
all_symbols=letters + numbers
length=int(input("Введите какой длинны нужен пороль - "))
password=""
for i in range(length):
    password+=random.choice(all_symbols)
print(password)


