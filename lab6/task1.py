import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

n = int(round((b - a) / h)) + 1
for i in range(n):
    x = a + i * h
    y = x * math.sin(x) + math.exp(x)
    print("x=%.2f  f(x)=%.4f" % (x, y))