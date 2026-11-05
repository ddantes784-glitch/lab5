n = int(input("Введите число: "))
original = n
facs = []

divisor = 2
while divisor * divisor <= n:
    # пока число делится на простой множитель
    while n % divisor == 0:
        facs.append(divisor)
        n //= divisor
    divisor += 1

if n > 1:
    facs.append(n)
print(f"{original} = {' × '.join(map(str, facs))}")
