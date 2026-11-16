import random
import string
import time

#Добавляю переменные
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

#Объединяю все воедино но с оговоркой,что ,до опроса пользователя, все символы=только набор букв с разным регистром 
all_symbols=letters

#Спрашиваю какой длинны нужен пароль
length=int(input("Введите какой длинны нужен пароль - "))
password=""

#Спрашиваю нужны ли цифры
need_numbers=(input("Нужны ли цифры? (Да/Нет): "))
if need_numbers.lower() == "да":
    all_symbols+=numbers

#Спрашиваю нужны специальные символы
need_special_symbols=(input("Нужны ли специальные символы? (Да/Нет): "))
if need_special_symbols.lower() == "да":
    all_symbols+=symbols

#Рассчитываю какой длинны будет пароль
for i in range(length):
    password+=random.choice(all_symbols)

#Создаю иллюзию загрузки(чисто интерактивная тема, на программу не влияет)
for a in range(5):
    print("Генерирую пароль.  ", end="\r")
    time.sleep(0.3)
    print("Генерирую пароль.. ", end="\r")
    time.sleep(0.3)
    print("Генерирую пароль...", end="\r")
    time.sleep(0.3)
    print("Генерирую пароль.. ", end="\r")
    time.sleep(0.3)
    print("Генерирую пароль.  ", end="\r")
print("Пароль готов!       ")
#Печатаю пароль
print(password)
