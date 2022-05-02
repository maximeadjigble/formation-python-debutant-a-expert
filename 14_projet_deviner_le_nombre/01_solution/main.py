import random

selection = random.randint(1,10)

nombre = 0
tentative = 0
tentatives_max = 5

while nombre != selection:
    if tentative >= tentatives_max:
        print("Vous avez perdu, le nombre est:", selection)
        break

    nombre = int(input("Entrez votre nombre [1-10] "))

    if selection > nombre:
        print("C'est plus")
    elif selection < nombre:
        print("C'est moins")
    else:
        print("Bravo, vous avez trouvé le nombre")

    tentative += 1