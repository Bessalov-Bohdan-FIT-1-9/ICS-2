import geometry

a = float(input("Введіть сторону трикутника a: "))

r1 = geometry.r_opysane(a)
r2 = geometry.r_vpysane(a)

print("Радіус кола, описаного навколо трикутника:", r1)
print("Радіус кола, вписаного в трикутник:", r2)