nom_complet = "Angelina Jolie"
# nom_complet = "brad pitt"

nom_complet_list = nom_complet.split(" ")
# print(nom_complet_list[0][0], nom_complet_list[1][0])
initiales = nom_complet_list[0][0] + nom_complet_list[1][0]
# print(initiales)
initiales = initiales.upper()
print(f"Les initiales de {nom_complet} sont: {initiales}")