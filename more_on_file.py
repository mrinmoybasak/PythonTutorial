f = open("mrinmoy2.txt")

f.seek(7)
f.tell()
print(f.readlines())
print(f.readlines())

f.close()