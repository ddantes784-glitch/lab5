n = int(input("Введите число n: "))
# присваиваем начальные значения
summ = 0
fact = 1
summsq = 0
# вводим цикл
for i in range(1, n + 1):
    summ += i
    fact *= i
    summsq += i**2
# выводим ответ
print(f"Сумма: {summ}")
print(f"Произведение (N!): {fact}")
print(f"Сумма квадратов: {summsq}")
