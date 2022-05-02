from Site.articles import Article
from Site.utilisateurs import Utilisateur

axel = Utilisateur("Axel", "Tony", 36)
# axel.info()
 
article = Article("Titre", "Contenu de l'article", axel)
article.afficher()