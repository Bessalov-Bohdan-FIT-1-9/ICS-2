import requests

urls = [
    "https://share.google/xuAvvlyo2Expt23K3",
    "https://share.google/fB8YyPeJsJeEiZQvh",
    # ... ще 8 посилань
]

for i, url in enumerate(urls, start=1):
    response = requests.get(url)
    if response.status_code == 200:
        filename = "db_image" + str(i) + ".jpg"
        with open(filename, "wb") as f:
            f.write(response.content)
        print("Завантажено:", filename)