def conversion(distance, unite):   
    taux_conversion = {"km": 0.001, "hm":0.01, "dam": 0.1, "m": 1, "dm":10, "cm": 100, "mm": 1000}
    if unite in taux_conversion:
        resultat = distance*taux_conversion[unite]
        print(f"Conversion: {distance} m = {resultat} {unite}")
    else:
        print("Unité invalide")

conversion(5.2, "km")