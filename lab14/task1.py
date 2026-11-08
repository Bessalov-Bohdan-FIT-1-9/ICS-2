import requests
from bs4 import BeautifulSoup

url = input("Введіть посилання на профіль у Google Scholar: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

r = requests.get(url, headers=headers)

if r.status_code == 200:
    soup = BeautifulSoup(r.text, "html.parser")
    links = soup.find_all("a")

    f = open("links.txt", "w", encoding="utf-8")
    for link in links:
        text = link.get_text().strip()
        if text:
            f.write(text + "\n")
    f.close()
    print("Готово: тексти посилань записано у links.txt")
else:
    print("Помилка доступу до сторінки, код:", r.status_code)