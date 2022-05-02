with open('fichier.txt', encoding='utf-8') as f:
    lignes = f.read().splitlines()
    mots = ' '.join(lignes).split(' ')
    # print(mots)
    nuage_mots = {}
    for m in mots:
        if m in nuage_mots:
            nuage_mots[m] += 1
        else:
            nuage_mots[m] = 1
    print(nuage_mots)