import tkinter as tk


def load_file():
    filename = entry_name.get()
    try:
        f = open(filename, "r", encoding="utf-8")
        content = f.read()
        f.close()
        text_box.delete("1.0", tk.END)
        text_box.insert("1.0", content)
    except FileNotFoundError:
        text_box.delete("1.0", tk.END)
        text_box.insert("1.0", "Файл не знайдено: " + filename)


win = tk.Tk()
win.title("Перегляд текстового файла")
win.geometry("600x350")
win.configure(background="blue")

lb = tk.Label(win, text="Назва файла:", fg="white", bg="blue")
lb.place(x=20, y=20)

entry_name = tk.Entry(win, width=40)
entry_name.place(x=140, y=22)
entry_name.insert(0, "input.txt")

button = tk.Button(win, text="Показати", command=load_file)
button.place(x=420, y=18)

text_box = tk.Text(win, width=70, height=15)
text_box.place(x=20, y=60)

win.mainloop()