distance = float(input("Entrez une distance (m) "))
unite = input("Entrez l'unité (km, cm ou mm) ")

taux_conversion = {"km": 0.001, "cm": 100, "mm": 1000}

if unite in taux_conversion:
    resultat = distance*taux_conversion[unite]
    print(f"Conversion: {distance} m = {resultat} {unite}")
else:
    print("Unité invalide")