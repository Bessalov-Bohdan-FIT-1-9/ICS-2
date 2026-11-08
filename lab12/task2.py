import random
import string


def generate_number():
    digits = "".join(random.choice(string.digits) for _ in range(4))
    letters = "".join(random.choice(string.ascii_uppercase) for _ in range(3))
    return digits + " " + letters


n = int(input("Скільки номерів згенерувати? N = "))
for i in range(n):
    print(generate_number())