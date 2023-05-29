# 1 Напишите программу, где я ввожу логин и пароль. И если данные были введены верно,
# то мы выводим Authentication completed, иначе Invalid login or password.
# (Логин должен быть user, пароль - qwerty)

login1 = input("введите логин: ")
password1 = input("введите пароль: ")
login2 = "user"
password2 = "qwerty"
if login1 == login2 and password1 == password2:
    print("Authentication completed")
else:
    print("Invalid login or password")

# задача 2 Напишите программу обмена валют, где я ввожу сумму в тенге и
# выбираю на какую валюту хочу перевести. (Курс USD – 420, EUR – 510, RUB - 5.8).

dict = {
    "USD" : 420,
    "EUR" : 510,
    "RUB" : 5.8
}
money_kz = float(input("введите сумму в тенге: "))

print("доступные валюты: USD, EUR, RUB")
сurrency = input("выберите валюту обмена: ")
if сurrency in dict :
    result = money_kz / dict[сurrency]
    print(f"{money_kz} равно {result}")
else:
    print("данная валюта не поддерживается")


# задача 3 Создать массив чисел от 0 до 1000, затем создать второй массив с их квадратами.(тут нужно использовать цикл for)
a = []
for i in range(1, 1000+1):
    a.append(i)
print(a)

# задача 4
a = []
for i in range(1, 1000+1):
    a.append(i**2)
print(a)

