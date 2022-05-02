with open('fichier.txt', encoding="utf-8") as f:
    lignes = f.read()
    # print(lignes[::-1])
    with open('fichier_crypt.txt', 'w', encoding="utf-8") as fw:
        fw.write(lignes[::-1])