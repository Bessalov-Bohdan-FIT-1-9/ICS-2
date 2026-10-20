import json
from datetime import date

cities = {
    "Київ": 482,
    "Львів": 1256,
    "Харків": 1654,
    "Одеса": 1794,
    "Дніпро": 1776,
    "Запоріжжя": 1770,
}

with open("cities.json", "w", encoding="utf-8") as f:
    json.dump(cities, f, ensure_ascii=False, indent=4)
print("Дані збережено у файл cities.json")

with open("cities.json", "r", encoding="utf-8") as f:
    data = json.load(f)

oldest = min(data, key=data.get)          # найменший рік заснування
age = date.today().year - data[oldest]
print(f"Найстаріше місто: {oldest}, засноване у {data[oldest]} р., вік: {age} р.")