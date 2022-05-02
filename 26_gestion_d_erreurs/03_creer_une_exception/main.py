import math

# https://docs.python.org/fr/3/library/exceptions.html#exception-hierarchy
def perimetre(rayon):
    if type(rayon) != float:
        raise TypeError("Le rayon doit être un nombre")
    if rayon < 0:
        raise ValueError("Le rayon doit être positif")
        # raise Exception("Le rayon doit être positif")
    return 2*math.pi*rayon
 
v = perimetre(10)
print(v)