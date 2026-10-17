A = set(range(2, 41, 2))
B = set(range(3, 41, 3))

C = A & B

D = set()
for x in A | B:
    if x % 12 == 0:
        D.add(x)

print("Множина A:", sorted(A))
print("Множина B:", sorted(B))
print("Множина C (діляться на 2 і на 3):", sorted(C))
print("Множина D (діляться на 12):", sorted(D))