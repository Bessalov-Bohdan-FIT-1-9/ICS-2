import sys
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
V = a * b * c
S = 2 * (a * b + b * c + a * c)
print("Об'єм =", V)
print("Площа поверхні =", S)