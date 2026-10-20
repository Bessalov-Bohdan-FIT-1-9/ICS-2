f = open("input.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

s1 = open("s1.txt", "w", encoding="utf-8")
s2 = open("s2.txt", "w", encoding="utf-8")

number = 1
for line in lines:
    if number % 2 == 0:
        s1.write(line)
    else:
        s2.write(line)
    number = number + 1

s1.close()
s2.close()
print("Готово: парні рядки записано у s1.txt, непарні у s2.txt")