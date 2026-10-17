s = input("Введіть рядок слів, розділених пробілами: ")
words = s.split()

shortest = min(words, key=len)
print("Найкоротше слово:", shortest)

if shortest.lower() == shortest.lower()[::-1]:
    print("Це слово є паліндромом")
else:
    print("Це слово не є паліндромом")