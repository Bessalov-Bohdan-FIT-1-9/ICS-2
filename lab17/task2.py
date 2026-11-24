import pandas as pd

months = ("Січень", "Лютий", "Березень", "Квітень", "Травень", "Червень",
          "Липень", "Серпень", "Вересень", "Жовтень", "Листопад", "Грудень")

counts = []
for month in months:
    n = int(input("Введіть кількість бетонних плит за " + month + ": "))
    counts.append(n)

s = pd.Series(counts, index=months)
print("\nМасив Series:")
print(s)

s.to_json("beton.json", force_ascii=False)
print("\nЗбережено у файл beton.json")