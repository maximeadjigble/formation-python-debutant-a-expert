#pierre gagne contre ciseaux
#papier gagne contre pierre
#ciseaux gagnent contre papier

import random

options = ["pierre", "papier", "ciseaux"]
selection_rand = random.choice(options)

choix = input("Sélectionnez pierre, papier ou ciseaux ")

if choix in options:
    if choix == selection_rand:
        print("Egalité")
    else:
        if (choix == "pierre" and selection_rand == "ciseaux") \
        or (choix == "papier" and selection_rand == "pierre") \
        or (choix == "ciseaux" and selection_rand == "papier"):
            print("Bravo, vous avez gagné")
        else:
            print("Vous avez perdu")

    print("Choix de l'ordinateur:", selection_rand)
else:
    print("Choix incorrect: options - pierre, papier, ciseaux")