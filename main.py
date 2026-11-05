eps = float(input("Введите точность: "))

e = 1.0
f = 1
i = 1

while True:
    step = 1 / f
    if step < eps:
        break
    e += step
    i += 1
    f *= i

print(f"Результат e: {e}")
