print("#1")
print(type(10 / 2))

print("#2")
print(bool(0.0))

print("#3")
x = 0
y = 12
print(x or y)

print("#4")
print(r"//\\")

print("#7")
print("a" * 3)

print("#8")
string = "привет"
print(string[::-1])

print("#9")
print(string[:])

print("#10")
print(bool(""))

print("#12")
print(string.encode())
print(string.encode().decode())

print("#14")
x = "Москва"
if "ква" not in x:
    print("1")
elif "ва" not in x:
    print("2")
else:
    print("3")

print("#16")
s = ""

for i in range(2, 10, 2):
    s += str(i)

print(s)
