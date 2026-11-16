import random
import string
import time
import colorama
from colorama import init, Fore
init(autoreset=True)

#Добавляю переменные
letters=string.ascii_letters
numbers=string.digits
symbols=string.punctuation

#Объединяю все воедино но с оговоркой,что ,до опроса пользователя, все символы=только набор букв с разным регистром 
all_symbols=letters

#Добавляю "корзину для пароля"
password=""

#Спрашиваю какой длинны нужен пароль(+ программа делает проверку, чтоб программа не рухнула)
while True:
    try:
       length = int(input("Введите длину пароля: "))
       if length > 0:
           break
       else:
           print("Число должно быть больше нуля!")
    except ValueError:
        print(Fore.RED + "Ошибка! Введите число цифрой.")

#Спрашиваю нужны ли цифры
while True:
    need_numbers=(input("Нужны ли цифры? (Да/Нет): "))
    if need_numbers.lower() == "да":
        all_symbols+=numbers
        break
    elif need_numbers.lower() == "нет":
        break
    print(Fore.RED + "Ошибка! Нужно ввести именно 'да' или 'нет'. Попробуйте еще раз.")

#Спрашиваю нужны специальные символы
while True:
    need_special_symbols=(input("Нужны ли специальные символы? (Да/Нет): "))
    if need_special_symbols.lower() == "да":
        all_symbols+=symbols
        break
    elif need_special_symbols.lower() == "нет":
        break
    print(Fore.RED + "Ошибка! Нужно ввести именно 'да' или 'нет'. Попробуйте еще раз.")

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
print(Fore.GREEN + "Пароль готов!       ")
#Печатаю пароль
print(password)