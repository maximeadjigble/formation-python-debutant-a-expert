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
    # print(nuage_mots)
    # print(nuage_mots.items())
    nuage_mots = dict(sorted(nuage_mots.items(), key=lambda item: item[1], reverse=True))
    print(nuage_mots)