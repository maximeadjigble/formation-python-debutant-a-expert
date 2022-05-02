# import blog
# from blog import Utilisateur
# from blog import Article
from blog import Utilisateur, Article


# axel = blog.Utilisateur("Axel", "Stark", 36)
axel = Utilisateur("Axel", "Tony", 36)
# axel.info()
# axel.ajouter()
 
article = Article("Titre", "Contenu de l'article", axel)
article.afficher()