countries = []
for i in range(10):
    name = input("Введіть назву країни Європи " + str(i + 1) + ": ")
    countries.append(name)

countries = tuple(countries)
print("Кортеж країн:", countries)