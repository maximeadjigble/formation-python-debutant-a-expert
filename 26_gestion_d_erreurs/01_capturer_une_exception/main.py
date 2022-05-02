try:
    with open('monfichier.txt') as f:
        texte = f.read()
        print(texte)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé")
# except Exception:
#     print("Une erreur s'est produite...")
print("Fin du Code")