n = 5

# прямоугольник
print("Прямоугольник:")
for i in range(n):
    print("*" * n)

# Треугольник
print("\n Треугольник:")
for i in range(1, n + 1):
    print("*" * i)

# Ёлочка
print("\n Ёлочка:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# Ромб
print("\n Ромб:")
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))
