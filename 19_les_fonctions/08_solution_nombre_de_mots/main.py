def nombre_mots(texte):
    mots = texte.split(" ")
    return len(mots)


# n = nombre_mots("Bonjour à toutes et à tous")
n = nombre_mots("La série d'essais quoi de neuf dans Python reprend les plus importants changements entres les versions majeures de Python. Elles sont à lire pour quiconque souhaitant être à jour suite à une nouvelle sortie")
print("le nombre de mots est:", n)