'''
# TODO 1
# Функция plus_two() выполняет одну простую задачу — выводит результат сложения переданного в нее числа 2 и значения
# переменной number. В переменную number должно быть передано число. Обработайте ситуацию, если в эту переменную переданы данные
# какого-то другого типа. В случае ошибки напечатайте в консоли сообщение «Ожидаемый тип данных — число!».

piteg = int(input("Введите число: "))


def plus_two(piteg):
    try:
        result = 2 + int(piteg)
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")


plus_two(piteg)
'''
'''
#TODO 2
#Напишите программу, которая позволяет получить доступ к элементу массива, индекс которого выходит за границы,
# и обработаем соответствующее исключение.

mass = [1, 3, 4]

try:
    print(mass[22])
except IndexError:
    print("Индекс выходит за рамки массива")
    
'''
import requests
import json

number = int(input("Введите число: "))

url = f"https://jsonplaceholder.typicode.com/todos/{number}"

try:
    response = requests.get(url)
    response.raise_for_status()

    todo = response.json()

    filename = f"{todo['id']}.json"
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(todo, file)
    print(f"Данные сохранены в файл: {filename}")
except Exception as error:
    print(error)
    print("Ошибка")
