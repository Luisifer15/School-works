x = [2, 5, 13, 17, 3, 89, 3, 5, 2, 90, 5, 65]
total = 0

x.append(42)
x.remove(89)
x.remove(90)
x.remove(65)

for i in range(len(x)):
    total += x[i]

print('The sum of all elements is', total)
input("Press Enter to exit")