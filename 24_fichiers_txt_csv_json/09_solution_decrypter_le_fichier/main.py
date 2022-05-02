with open('fichier_crypt.txt', encoding="utf-8") as f:
    lignes = f.read()
    print(lignes[::-1])