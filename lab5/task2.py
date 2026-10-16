a = int(input("Введіть перше число: "))
b = int(input("Введіть друге число: "))
c = int(input("Введіть третє число: "))

if (a >= b and a <= c) or (a <= b and a >= c):
    middle = a
elif (b >= a and b <= c) or (b <= a and b >= c):
    middle = b
else:
    middle = c

print("Середнє число:", middle)