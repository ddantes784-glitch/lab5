from random import *
n = randint(1000, 9999)
from random import *
n = randint(1000, 9999)
# Переводим загаданное число в строку для удобного сравнения
secret = str(n)

print("Компьютер загадал 4-значное число. Попробуйте угадать")

while True:
    guess = input("Введите ваш вариант (4 цифры): ").strip()
    
    if len(guess) != 4 or not guess.isdigit():
        print("Пожалуйста, введите 4 цифры.")
        continue
        
    if guess == secret:
        print(f"Поздравляем! Вы угадали число {secret}!")
        break
        
    bulls = 0
    cows = 0
    
    # Считаем быков и коров
    for i in range(4):
        if guess[i] == secret[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
            
    print(f"Быки: {bulls}, Коровы: {cows}")
