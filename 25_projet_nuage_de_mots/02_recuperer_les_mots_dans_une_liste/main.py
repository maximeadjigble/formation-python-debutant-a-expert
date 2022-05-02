with open('fichier.txt', encoding='utf-8') as f:
    lignes = f.read().splitlines()
    print(lignes)
    mots = ' '.join(lignes).split(' ')
    print(mots)