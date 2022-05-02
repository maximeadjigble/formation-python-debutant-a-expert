try:
    with open('monfichier.txt') as f:
        texte = f.read()
        print(texte)
        volume = float(texte)
except FileNotFoundError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("Fin du Code")