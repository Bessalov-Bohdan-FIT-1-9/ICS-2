import math


def func(x, a, b):
    F = x * math.tan(x) * math.exp(a - b) + math.log(abs(x ** 2 + 0.7), 4)
    return F


x = float(input("Введіть x: "))
a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
print("F =", func(x, a, b))