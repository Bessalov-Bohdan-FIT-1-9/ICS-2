import tkinter as tk


def det3(a1, b1, c1, a2, b2, c2, a3, b3, c3):
    return (a1 * (b2 * c3 - b3 * c2)
            - b1 * (a2 * c3 - a3 * c2)
            + c1 * (a2 * b3 - a3 * b2))


def solve():
    try:
        a1 = float(e_a1.get()); b1 = float(e_b1.get()); c1 = float(e_c1.get()); d1 = float(e_d1.get())
        a2 = float(e_a2.get()); b2 = float(e_b2.get()); c2 = float(e_c2.get()); d2 = float(e_d2.get())
        a3 = float(e_a3.get()); b3 = float(e_b3.get()); c3 = float(e_c3.get()); d3 = float(e_d3.get())

        D = det3(a1, b1, c1, a2, b2, c2, a3, b3, c3)
        if D == 0:
            result_label.config(text="Система не має єдиного розв'язку")
            return

        Dx = det3(d1, b1, c1, d2, b2, c2, d3, b3, c3)
        Dy = det3(a1, d1, c1, a2, d2, c2, a3, d3, c3)
        Dz = det3(a1, b1, d1, a2, b2, d2, a3, b3, d3)

        x = Dx / D
        y = Dy / D
        z = Dz / D

        result_label.config(text="x = %.4f, y = %.4f, z = %.4f" % (x, y, z))
    except ValueError:
        result_label.config(text="Введіть коректні числа")


win = tk.Tk()
win.title("Система лінійних рівнянь 3-го порядку")

frame = tk.Frame(win)
frame.pack(padx=10, pady=10)

tk.Label(frame, text="a1x + b1y + c1z = d1").grid(row=0, column=0, columnspan=4)
e_a1 = tk.Entry(frame, width=5); e_a1.grid(row=1, column=0)
e_b1 = tk.Entry(frame, width=5); e_b1.grid(row=1, column=1)
e_c1 = tk.Entry(frame, width=5); e_c1.grid(row=1, column=2)
e_d1 = tk.Entry(frame, width=5); e_d1.grid(row=1, column=3)

tk.Label(frame, text="a2x + b2y + c2z = d2").grid(row=2, column=0, columnspan=4)
e_a2 = tk.Entry(frame, width=5); e_a2.grid(row=3, column=0)
e_b2 = tk.Entry(frame, width=5); e_b2.grid(row=3, column=1)
e_c2 = tk.Entry(frame, width=5); e_c2.grid(row=3, column=2)
e_d2 = tk.Entry(frame, width=5); e_d2.grid(row=3, column=3)

tk.Label(frame, text="a3x + b3y + c3z = d3").grid(row=4, column=0, columnspan=4)
e_a3 = tk.Entry(frame, width=5); e_a3.grid(row=5, column=0)
e_b3 = tk.Entry(frame, width=5); e_b3.grid(row=5, column=1)
e_c3 = tk.Entry(frame, width=5); e_c3.grid(row=5, column=2)
e_d3 = tk.Entry(frame, width=5); e_d3.grid(row=5, column=3)

button = tk.Button(win, text="Розв'язати", command=solve)
button.pack(pady=5)

result_label = tk.Label(win, text="")
result_label.pack(pady=5)

win.mainloop()