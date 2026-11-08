def rhombus(width, height):
    mid = (height - 1) / 2
    for i in range(height):
        distance = abs(i - mid)
        stars = round(width * (1 - distance / (mid + 0.5)))
        if stars < 1:
            stars = 1
        spaces = (width - stars) // 2
        print(" " * spaces + "*" * stars)


w = int(input("Введіть ширину ромба: "))
h = int(input("Введіть висоту ромба: "))
rhombus(w, h)