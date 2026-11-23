import pylab

alphabet = "абвгґдежзиіїйклмнопрстуфхцчшщьюя"

f = open("input.txt", "r", encoding="utf-8")
text = f.read().lower()
f.close()

counts = []
for letter in alphabet:
    counts.append(text.count(letter))

pylab.bar(list(alphabet), counts)
pylab.xlabel("Літера")
pylab.ylabel("Кількість")
pylab.title("Частота українських літер у тексті")
pylab.show()