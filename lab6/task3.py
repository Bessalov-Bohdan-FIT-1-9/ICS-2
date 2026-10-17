import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть крок h: "))

spisok = []
x = a
while x <= b + 1e-9:
    y = x * math.sin(x) + math.exp(x)
    spisok.append(round(y, 4))
    x = x + h

print("Список:", spisok)
spisok.sort()
print("Відсортований список:", spisok)