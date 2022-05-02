# def ma_fonction():
#     print("Bonjour Georges")
#     print("Ok")

# ma_fonction()
# ma_fonction()
# ma_fonction()

def devinez_le_nombre():
    import random

    selection = random.randint(1,10)

    nombre = 0
    tentatives_max = 5
    tentatives = 0
    while nombre != selection:
        if tentatives >= tentatives_max:
            print("Vous avez perdu, le nombre est:", selection)
            break
            
        nombre = int(input("Entrez votre nombre "))
        
        if selection > nombre:
            print("C'est plus")
        elif selection < nombre:
            print("C'est moins")
        else:
            print("Bravo, vous avez trouvé le nombre")

        tentatives+=1

devinez_le_nombre()