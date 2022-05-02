import csv

celebrites = [["John","Travolta",  67], ["Halle","Berry", 54], ["Dwayne", "Johnson", 48]]

with open('celebrites.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Prenom", "Nom", "Age"])
    writer.writerow(celebrites[0])
    writer.writerow(celebrites[1])
    writer.writerow(celebrites[2])