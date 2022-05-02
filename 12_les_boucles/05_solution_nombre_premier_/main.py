nombre = int(input("Entrez un nombre "))
divisible = False

for i in range(2, nombre):
    if (nombre % i) == 0:
        # print(i)
        divisible = True
        break

if divisible:
    print(f"{nombre} n'est pas un nombre premier")
else:
    print(f"{nombre} est un nombre premier")