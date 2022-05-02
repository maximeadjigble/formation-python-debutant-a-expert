# Poids en kg et taille en m
# imc = poids/taille^2 

poids = float(input('Entrez votre poids (Kg): '))
taille = float(input('Entrez votre taille (m): '))
imc = poids/(taille**2)
print(f"L'IMC d'une personne de {poids} Kg & {taille} m est {imc} Kg/m^2")