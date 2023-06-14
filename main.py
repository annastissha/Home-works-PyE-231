
# todo Напишите программу которая будет шифровать текст шифром Цезаря.
'''
alphabet = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
encrypt = input("Enter a clear message: ")
key = int(input("Enter a key (number from 1-25): "))
encrypt = encrypt.lower()
encrypted = ""
for letter in encrypt:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet: #проверка символа
        encrypted = encrypted + alphabet[newPosition] #после смещения новая буква добавляется у к шифр. сообщению
    else:
        encrypted = encrypted + letter
print("Your cipher is: ", encrypted)
'''
# todo 2 вариант решения
'''
encrypt = input("Enter a clear message: ")
shift = int(input("Enter a shift key : "))

encrypted_text = ""

for char in encrypt:
    if char == "":
        encrypted_text += ""
    else:
        ascii_code = ord(char)
        if shift > 0:
            new_ascii_code = ascii_code + shift
            if new_ascii_code > ord("z"):
                new_ascii_code -= 26
        else:
            new_ascii_code = ascii_code + shift
            if new_ascii_code < ord("a"):
                new_ascii_code += 26
        encrypted_text += chr(new_ascii_code)

print("Your cipher is: ", encrypted_text)
'''

#2 Пользователь вводит с клавиатуры название фрукта. Необходимо вывести на экран количество раз, сколько фрукт
# встречается в кортеже в качестве элемента.
'''
fruits = ('apple', 'orange', 'banana', 'grape', 'grape', 'apple', 'plum')
fruit = input("Введите название фрукта: ")
count = fruits.count(fruit)
print("Фрукт", fruit, "встречается", count, "раз в кортеже" )
'''
#Добавьте к заданию 1 подсчет количества раз, когда название фрукта является частью элемента.
'''
fruits = ('orange', 'banana', 'grape', 'grape', 'apple', 'plum', 'banana', 'apple', 'bananamango', 'mango', 'strawberry-banana')
fruit = input("Введите название фрукта: ")
count_exact = fruits.count(fruit)
count_partial = sum(1 for f in fruits if fruit in f)

print("Фрукт", fruit, "встречается", count_exact, "раз в кортеже" )
'''

#Есть кортеж с названиями производителей автомобилей (название производителя может встречаться от 0 до N раз).
# Пользователь вводит с клавиатуры название производителя и слово для замены. Необходимо заменить в кортеже все элементы
#с этим названием на слово для замены. Совпадение по названию должно быть полным.
'''
car_brands = ('Toyota', 'Honda', 'Ford', 'Toyota', 'Chevrolet')
old_brand = input('Введите название производителя: ')
new_brand = input('Введите слово для замены: ')

new_car_brands = tuple(new_brand if brand == old_brand else brand for brand in car_brands)

print(new_car_brands)
'''
# todo Множества
#1 Напишите функцию superset(), которая принимает 2 множества. Результат работы
#функции: вывод в консоль одного из сообщений в зависимости от ситуации:
'''
set1 = set(input("Введите первое множество через запятую: ").split(","))
set2 = set(input("Введите второе множество через запятую: ").split(","))

def superset(set1, set2):
    if set1.issuperset(set2):
        if set1 == set2:
            print(f"Множества  {set1} равны")
        else:
            print(f"Объект {set1} является супермножеством, но содержит дополнительные элементы")
    else:
        print("Супермножество не обнаружено")
superset(set1, set2)
'''
# todo
import json
from datetime import datetime

day1 = input("Введите первый день недели: ")
day2 = input("Введите второй день недели: ")


date1 = datetime.strptime(day1, '%A')
date2 = datetime.strptime(day2, '%A')

if date1 > date2:
    hours_left = (date2 - date1).days * 24
else:
    hours_left = (date2 - date1).days * 24


print(f"До наступления большей даты осталось {int(hours_left)} часов")

data = {"date1": date1.strftime("%Y-%m-%d"), "date2": date2.strftime("%Y-%m-%d")}
with open("dates.json", "w") as f:
    json.dump(data, f)
