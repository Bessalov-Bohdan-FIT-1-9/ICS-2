import pandas as pd

fname = "production.csv"
df = pd.read_csv(fname, sep=";", encoding="utf-8")
print("Таблиця до доповнення:")
print(df)

new_rows = pd.DataFrame({
    "Місяць": ["Липень", "Серпень", "Вересень"],
    "Фірма1": [148, 152, 160],
    "Фірма2": [118, 122, 125],
    "Фірма3": [158, 162, 170],
})

df = pd.concat([df, new_rows], ignore_index=True)

print("\nТаблиця після доповнення:")
print(df)

df.to_csv("all.csv", sep=";", encoding="utf-8", index=False)
print("\nЗбережено у файл all.csv")