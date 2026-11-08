class Auto:
    def __init__(self, model, manufacturer, year):
        self.model = model
        self.manufacturer = manufacturer
        self.year = year

    def set_year(self, new_year):
        self.year = new_year

    def show(self):
        print("Модель:", self.model, "| Виробник:", self.manufacturer, "| Рік випуску:", self.year)


autos = []

n = int(input("Скільки автомобілів додати? N = "))
for i in range(n):
    model = input("Введіть модель: ")
    manufacturer = input("Введіть виробника: ")
    year = int(input("Введіть рік випуску: "))
    autos.append(Auto(model, manufacturer, year))

print("\nСписок автомобілів:")
for car in autos:
    car.show()

search = input("\nВведіть модель для пошуку: ")
found = False
for car in autos:
    if car.model == search:
        print("Знайдено:")
        car.show()
        found = True
if not found:
    print("Автомобіль з такою моделлю не знайдено")