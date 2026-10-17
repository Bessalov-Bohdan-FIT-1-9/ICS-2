import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

x = a
while x <= b + 1e-9:
    y = x * math.sin(x) + math.exp(x)
    print("x=%.2f  f(x)=%.4f" % (x, y))
    x = x + h