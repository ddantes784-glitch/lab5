n = int(input("Введите число: "))
original = n
# ввод переменных
count = 0
total = 0
product = 1
revers = 0
# ввод цикла while
while n > 0:
    digit = n % 10
    count += 1
    total += digit
    product *= digit
    revers = revers * 10 + digit
    n //= 10
# вывод полученных результатов
print(f"Количество цифр: {count}")
print(f"Сумма цифр: {total}")
print(f"Произведение цифр: {product}")
print(f"Перевернутое число: {revers}")
