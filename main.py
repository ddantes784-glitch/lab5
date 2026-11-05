import random

def estimate_pi(num_samples):
    inside_circle = 0

    for _ in range(num_samples):
        # Генерируем случайную точку (x, y) в квадрате от 0 до 1
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Проверяем, попала ли точка внутрь четверти круга
        # (используем уравнение окружности x² + y² <= 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1

    # Вычисляем приближенное значение pi
    pi_estimate = 4 * inside_circle / num_samples
    return pi_estimate

# Количество случайных точек (чем больше, тем точнее результат)
samples = 1000000
calculated_pi = estimate_pi(samples)

print(f"Количество точек: {samples}")
print(f"Вычисленное значение π: {calculated_pi}")