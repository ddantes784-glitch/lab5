n = int(input("Введите число: "))
# ввод переменных
original = n
reversed_num = 0
temp = n
# ввод цикла while
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10
# ввод условия if
if original == reversed_num:
    print(f"{original} — палиндром")
else:
    print(f"{original} — не палиндром")
