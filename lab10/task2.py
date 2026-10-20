import os

files = os.listdir(".")
print("Вміст поточного каталога:")
for name in files:
    print(name)

f_files = []
for name in files:
    if name.startswith("f") and os.path.isfile(name):
        f_files.append(name)

print("Файли, які починаються з літери f:", f_files)