from array import *

m = int(input("Введіть число M: "))
n = int(input("Введіть кількість елементів N: "))

masiv = array('i', [])
for i in range(1, n + 1):
    masiv.append(m * i)

print(masiv)