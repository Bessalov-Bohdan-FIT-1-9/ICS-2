n = int(input("Введіть кількість рядків N: "))

best = ""
best_count = 0

for i in range(n):
    s = input("Введіть рядок " + str(i + 1) + ": ")
    count = 0
    for symbol in s:
        if s.count(symbol) > count:
            count = s.count(symbol)
    if count > best_count:
        best_count = count
        best = s

print("Рядок з найбільшою кількістю однакових символів:", best)
print("Кількість однакових символів:", best_count)