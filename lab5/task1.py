import math

x = float(input("Введіть x: "))

if x >= 3.7:
    f = x + math.sqrt(x) + (4 * x + 7) ** (1 / 3)
elif x > -1.5:
    f = math.tan(x) + x ** 2
else:
    f = math.log(abs(x))

print("f(x) =", f)