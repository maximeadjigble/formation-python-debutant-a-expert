import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Pong Clone')
pygame.display.set_icon(pygame.image.load('favicon.png'))
FPS = 60 
 
class Joueur:
    LARGEUR = 15
    HAUTEUR = 50

    def __init__(self, pos = (0,0)):
        self.rect = pygame.Rect(pos[0], pos[1], Joueur.LARGEUR, Joueur.HAUTEUR)

def dessiner(joueur_d, joueur_g, boule):
    fenetre.fill('black') 

    pygame.draw.rect(fenetre, 'white', joueur_g.rect)
    pygame.draw.rect(fenetre, 'white', joueur_d.rect)
    pygame.draw.rect(fenetre, 'white', boule)

    pygame.display.update()
 
joueur_g = Joueur((5, (HAUTEUR - Joueur.HAUTEUR)/2))
joueur_d = Joueur((LARGEUR - Joueur.LARGEUR - 5, (HAUTEUR - Joueur.HAUTEUR)/2))

DIM_BOULE = 10
boule = pygame.Rect(LARGEUR/2, HAUTEUR/2, DIM_BOULE, DIM_BOULE)

def main():
    executer = True
    clock = pygame.time.Clock()
    while executer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executer = False 
 
        dessiner(joueur_d, joueur_g, boule)
        clock.tick(FPS)
 
    pygame.quit()
 
 
if __name__ == "__main__":
    main()