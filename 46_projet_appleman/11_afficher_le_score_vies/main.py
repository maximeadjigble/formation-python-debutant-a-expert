import os
import sys
import pygame
import random
 
pygame.init()
pygame.mixer.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))
FPS = 60
VITESSE = 5

son_mange = pygame.mixer.Sound(os.path.join('assets', 'mange.wav'))
son_malade = pygame.mixer.Sound(os.path.join('assets', 'malade.wav'))

FONT = pygame.font.SysFont(None, 50)
N_BONNES_GAGNER = 5
N_VIES = 3

class Objet:
    def __init__(self, image_path, pos):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.image_path = image_path
    
    def recharger_image(self):
        self.image = pygame.image.load(self.image_path).convert_alpha()

    def blit(self, fenetre):
        fenetre.blit(self.image, self.rect)

    def en_collision(self, objet):
        return self.rect.colliderect(objet.rect)

    def changer_pos(self, pos):
        self.rect.center = pos

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

def generer_pos_aleatoire(objets):
    pos_x = 0
    pos_y = 0
    valide = False
    while not valide:
        valide = True
        pos_x = random.randint(25, LARGEUR-25)
        pos_y = random.randint(25, HAUTEUR-25)
        pos_obj = Objet(os.path.join('assets', 'pomme_bonne.png'), (pos_x, pos_y))
        for objet in objets:
            if pos_obj.en_collision(objet):
                valide = False
    return pos_x, pos_y

def dessiner(donnees):
    personne = donnees['personne']
    pomme_bonne = donnees['pomme_bonne']
    pommes_pourries = donnees['pommes_pourries']
    n_bonnes = donnees['n_bonnes']
    n_mauvaises = donnees['n_mauvaises']
        
    fenetre.fill('#c7f7be') 
    pomme_bonne.blit(fenetre)
    for p in pommes_pourries:
        p.blit(fenetre)
    personne.blit(fenetre)

    score = FONT.render(f'{n_bonnes}/{N_BONNES_GAGNER}', True, 'blue', 'white')
    vies = FONT.render(f'{N_VIES - n_mauvaises}', True, 'red', 'white')
    fenetre.blit(score, (LARGEUR - 100, 20))
    fenetre.blit(vies, (LARGEUR - 40, 20))
    pygame.display.update()

def main(): 
    joueur = Joueur()
    personne = joueur.defaut
    pomme_bonne = Objet(os.path.join('assets', 'pomme_bonne.png'), (50, 30))
    pommes_pourries = [Objet(os.path.join('assets', 'pomme_pourrie.png'), (300, 100))]
    
    n_bonnes = 0
    n_mauvaises = 0
    en_collision = False
    t_collision = 0
    debuter = False
    executer = True
    clock = pygame.time.Clock()
    while executer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executer = False 
                pygame.quit()
                sys.exit()

        if not en_collision:
            offset_x = personne.image.get_width()/2
            offset_y = personne.image.get_height()/2
            touches = pygame.key.get_pressed()
            if touches[pygame.K_z]: 
                personne.rect.y -= VITESSE
                if personne.rect.y + offset_y < 0:
                    personne.rect.y = HAUTEUR
            if touches[pygame.K_s]: 
                personne.rect.y += VITESSE
                if personne.rect.y + offset_y > HAUTEUR:
                    personne.rect.y = -2*offset_y
            if touches[pygame.K_q]: 
                personne.rect.x -= VITESSE
                if personne.rect.x + offset_x < 0:
                    personne.rect.x = LARGEUR
            if touches[pygame.K_d]: 
                personne.rect.x += VITESSE
                if personne.rect.x + offset_x > LARGEUR:
                    personne.rect.x = -2*offset_x

            if touches[pygame.K_z] \
                or touches[pygame.K_s] \
                or touches[pygame.K_d] \
                or touches[pygame.K_q]:
                personne.image = joueur.recuperer_image_marche()
            else:
                # personne.image = joueur.defaut.image
                personne.recharger_image()

        #Gestion des collisions
        if personne.en_collision(pomme_bonne):
            objets = [personne, pomme_bonne]
            objets.extend(pommes_pourries)
            pomme_bonne.changer_pos(generer_pos_aleatoire(objets))
            pommes_pourries.append(Objet(os.path.join('assets', 'pomme_pourrie.png'), generer_pos_aleatoire(objets)))
            son_mange.play()
            en_collision = True
            t_collision = pygame.time.get_ticks()
            personne.image = joueur.mange.image.copy()
            n_bonnes += 1

        nombre_avant = len(pommes_pourries)
        pommes_pourries = [p for p in pommes_pourries if not p.en_collision(personne)]
        if nombre_avant > len(pommes_pourries):
            son_malade.play()
            en_collision = True
            t_collision = pygame.time.get_ticks()
            personne.image = joueur.malade.image.copy()
            n_mauvaises += 1

        if en_collision and pygame.time.get_ticks() - t_collision > 400:
            en_collision = False

        donnees = {}
        donnees['personne'] = personne
        donnees['pomme_bonne'] = pomme_bonne
        donnees['pommes_pourries'] = pommes_pourries
        donnees['n_bonnes'] = n_bonnes
        donnees['n_mauvaises'] = n_mauvaises
        dessiner(donnees)
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()