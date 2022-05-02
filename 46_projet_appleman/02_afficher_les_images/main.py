import os
import sys
import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))
FPS = 60

class Objet:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)

    def blit(self, fenetre):
        fenetre.blit(self.image, self.rect)

def dessiner(donnees):
    personne = donnees['personne']
    pomme_bonne = donnees['pomme_bonne']
    pomme_pourrie = donnees['pomme_pourrie']

    fenetre.fill('#c7f7be') 
    personne.blit(fenetre)
    pomme_bonne.blit(fenetre)
    pomme_pourrie.blit(fenetre)

    pygame.display.update()

def main(): 
    personne = Objet(os.path.join('assets', 'personne.png'), (LARGEUR/2, HAUTEUR/2))
    pomme_bonne = Objet(os.path.join('assets', 'pomme_bonne.png'), (50, 30))
    pomme_pourrie = Objet(os.path.join('assets', 'pomme_pourrie.png'), (300, 100))
    
    debuter = False
    executer = True
    clock = pygame.time.Clock()
    while executer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executer = False 
                pygame.quit()
                sys.exit()

        donnees = {}
        donnees['personne'] = personne
        donnees['pomme_bonne'] = pomme_bonne
        donnees['pomme_pourrie'] = pomme_pourrie
        dessiner(donnees)
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()