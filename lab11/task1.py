import csv


def read_prices(filename):
    """Зчитує з CSV-файла словник «продукт: ціна»."""
    prices = {}
    with open(filename, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            prices[row["product"]] = float(row["price"])
    return prices


def write_prices(filename, prices):
    """Записує словник «продукт: ціна» у CSV-файл."""
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["product", "price"])
        for product, price in prices.items():
            writer.writerow([product, price])


prices = read_prices("products.csv")
print("Прочитано з products.csv:")
for product, price in prices.items():
    print(f"  {product}: {price} грн")

write_prices("prices_copy.csv", prices)
print("Дані збережено у файл prices_copy.csv")