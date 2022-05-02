import os
import sys
import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))
FPS = 60
VITESSE = 5

class Objet:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.image_path = image_path
    
    def recharger_image(self):
        self.image = pygame.image.load(self.image_path).convert_alpha()

    def blit(self, fenetre):
        fenetre.blit(self.image, self.rect)

class Joueur:
    def __init__(self):
        self.defaut = Objet(os.path.join('assets', 'personne.png'), (LARGEUR/2, HAUTEUR/2))
        self.marche = [
            Objet(os.path.join('assets', 'personne_marche_droite.png'), self.defaut.rect.center),
            Objet(os.path.join('assets', 'personne_marche_gauche.png'), self.defaut.rect.center)
        ]
        self.mange = Objet(os.path.join('assets', 'personne_mange.png'), self.defaut.rect.center)
        self.malade = Objet(os.path.join('assets', 'personne_malade.png'), self.defaut.rect.center)
        self.idx = 0

    def recuperer_image_marche(self, vitesse=0.1):
        self.idx += vitesse
        if self.idx >= len(self.marche):
            self.idx = 0
        return self.marche[int(self.idx)].image

def dessiner(donnees):
    personne = donnees['personne']
    pomme_bonne = donnees['pomme_bonne']
    pomme_pourrie = donnees['pomme_pourrie']

    fenetre.fill('#c7f7be') 
    pomme_bonne.blit(fenetre)
    pomme_pourrie.blit(fenetre)
    personne.blit(fenetre)

    pygame.display.update()

def main(): 
    joueur = Joueur()
    personne = joueur.defaut
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

        touches = pygame.key.get_pressed()
        if touches[pygame.K_z] and personne.rect.y > 0: 
            personne.rect.y -= VITESSE
        if touches[pygame.K_s] and personne.rect.y + personne.image.get_height() < HAUTEUR: 
            personne.rect.y += VITESSE
        if touches[pygame.K_q] and personne.rect.x > 0: 
            personne.rect.x -= VITESSE
        if touches[pygame.K_d] and personne.rect.x + personne.image.get_width() < LARGEUR: 
            personne.rect.x += VITESSE

        if touches[pygame.K_z] \
            or touches[pygame.K_s] \
            or touches[pygame.K_d] \
            or touches[pygame.K_q]:
             personne.image = joueur.recuperer_image_marche()
        else:
            # personne.image = joueur.defaut.image
            personne.recharger_image()

        donnees = {}
        donnees['personne'] = personne
        donnees['pomme_bonne'] = pomme_bonne
        donnees['pomme_pourrie'] = pomme_pourrie
        dessiner(donnees)
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()