villes = ["Paris","New York","Londres"]

ville = "Lyon"
if ville in villes:
    print(f"{ville} fait déjà partie de notre liste")
else:
    print(f"{ville} est rajouté à la liste")
    villes.append(ville)

print(villes)




# print("Paris" in villes)
# print("Lyon" in villes)