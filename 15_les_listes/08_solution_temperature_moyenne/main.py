temperatures = [23, 22, 19, 26, 24, 28, 26]

moyenne = 0
for t in temperatures:
    # moyenne = moyenne + t
    moyenne += t

moyenne = moyenne/len(temperatures) 

print(f"La température moyenne est de {moyenne}°C")
