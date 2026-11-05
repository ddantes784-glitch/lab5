from math import *
print(f"{'x':>8} {'sin(x)':>10}")
print('--'*10)
for i in range(10+1):
    x = i*pi
    y = sin(x)
    print(f"{x:8.4f} {y:10.4f}")