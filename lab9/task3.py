elements = {
    "H": 1.008,
    "He": 4.003,
    "Li": 6.94,
    "C": 12.011,
    "N": 14.007,
    "O": 15.999,
    "Na": 22.990,
    "Fe": 55.845,
}

n = int(input("Скільки елементів додати? N = "))
for i in range(n):
    symbol = input("Введіть позначення елемента: ")
    mass = float(input("Введіть атомну масу: "))
    elements[symbol] = mass

print("Словник за зростанням атомної маси:")
for symbol, mass in sorted(elements.items(), key=lambda item: item[1]):
    print(symbol, mass)