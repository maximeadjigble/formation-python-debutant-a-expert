import os

# Répertoire courant & liste de fichiers/dossiers
# print(os.getcwd())
# print(os.listdir('.vscode'))

#Changer de répertoire
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())

#Supprimer un fichier
# print(os.getcwd())
# os.remove('fichier.txt')
# print(os.listdir())

#Créer un dossier
# os.mkdir('test2')

#Supprimer un dossier
# os.removedirs('mondossier')
# os.removedirs('test')
# os.removedirs('test2')

#Construire un chemin
# path = os.path.join(os.getcwd(), 'fichier.txt')
# print(path)

print(os.cpu_count())