import math

x = float(input("Введіть x: "))
f = (x + math.sin(x)) / math.log10(abs(x - x ** 4)) + math.log(x, 4)
print("f(x) =", f)