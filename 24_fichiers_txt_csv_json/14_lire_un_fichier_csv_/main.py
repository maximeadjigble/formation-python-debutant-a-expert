import csv

with open('titanic.csv') as f:
    lecteur = csv.reader(f)
    # print(next(lecteur, None))
    for i, ligne in enumerate(lecteur):
        print(i, ligne[4])
        if i >= 5:
            break