import pygame
from random import randint
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Pong Clone')
pygame.display.set_icon(pygame.image.load('favicon.png'))
FPS = 60 

separateurs = []
N = 10
LARGEUR_SEP = 2
HAUTEUR_SEP = HAUTEUR/N
OFFSET = 20
for i in range(N):
    x = (LARGEUR - LARGEUR_SEP)/2
    y = i*HAUTEUR_SEP + OFFSET/2
    separateurs.append(pygame.Rect(x, y, LARGEUR_SEP, HAUTEUR_SEP - OFFSET))

VITESSE_BOULE = 5
VITESSE_BOULE_LENT = 2

class Joueur:
    LARGEUR = 15
    HAUTEUR = 50
    VITESSE = 5
    FONT = pygame.font.SysFont(None, 100)

    def __init__(self, pos = (0,0)):
        self.rect = pygame.Rect(pos[0], pos[1], Joueur.LARGEUR, Joueur.HAUTEUR)
        self.score = 0

    def deplacer_haut(self):
        self.rect.y -= Joueur.VITESSE

    def deplacer_bas(self):
        self.rect.y += Joueur.VITESSE

    def score_surface(self):
        return Joueur.FONT.render(str(self.score), True, 'white')


def gerer_collisions(boule, boule_dir, joueur_g, joueur_d):
    if boule.colliderect(joueur_g.rect) or boule.colliderect(joueur_d.rect):
        changer_vitesse_boule(boule_dir, VITESSE_BOULE)
        boule_dir.x = -boule_dir.x

def initialiser_boule(boule, boule_dir):
    boule.x = LARGEUR/2
    boule.y = randint(HAUTEUR/4, HAUTEUR - HAUTEUR/4)
    changer_vitesse_boule(boule_dir, VITESSE_BOULE_LENT)

def changer_vitesse_boule(boule_dir, vitesse):
    boule_dir.x = vitesse if boule_dir.x > 0 else -vitesse
    boule_dir.y = vitesse if boule_dir.y > 0 else -vitesse

def deplacer_boule(boule, boule_dir):
    if boule.x <= 0:
        joueur_d.score += 1
        initialiser_boule(boule, boule_dir)

    if boule.x + DIM_BOULE >= LARGEUR:
        joueur_g.score += 1
        initialiser_boule(boule, boule_dir)

    if boule.y <= 0 or boule.y + DIM_BOULE >= HAUTEUR:
        boule_dir.y = -boule_dir.y

    boule.x += boule_dir.x
    boule.y += boule_dir.y

def dessiner(joueur_d, joueur_g, boule):
    fenetre.fill('black') 

    for sep in separateurs:
        pygame.draw.rect(fenetre, 'white', sep)

    pygame.draw.rect(fenetre, 'white', joueur_g.rect)
    pygame.draw.rect(fenetre, 'white', joueur_d.rect)
    pygame.draw.rect(fenetre, 'white', boule)

    fenetre.blit(joueur_g.score_surface(), (LARGEUR/2 - 100, 10))
    score_surf = joueur_d.score_surface()
    fenetre.blit(score_surf, (LARGEUR/2 + 100 - score_surf.get_width(), 10))

    pygame.display.update()
 
joueur_g = Joueur((5, (HAUTEUR - Joueur.HAUTEUR)/2))
joueur_d = Joueur((LARGEUR - Joueur.LARGEUR - 5, (HAUTEUR - Joueur.HAUTEUR)/2))

DIM_BOULE = 10
boule = pygame.Rect(LARGEUR/2, HAUTEUR/2, DIM_BOULE, DIM_BOULE)
boule_dir = boule.copy()

def main():
    executer = True
    clock = pygame.time.Clock()
    initialiser_boule(boule, boule_dir)
    while executer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executer = False 

        touches = pygame.key.get_pressed()
        if touches[pygame.K_z] and joueur_g.rect.y > 0:
            joueur_g.deplacer_haut()
        if touches[pygame.K_s] and joueur_g.rect.y + Joueur.HAUTEUR < HAUTEUR:
            joueur_g.deplacer_bas()
        if touches[pygame.K_UP] and joueur_d.rect.y > 0:
            joueur_d.deplacer_haut()
        if touches[pygame.K_DOWN] and joueur_d.rect.y + Joueur.HAUTEUR < HAUTEUR:
            joueur_d.deplacer_bas()

        gerer_collisions(boule, boule_dir, joueur_g, joueur_d)
        deplacer_boule(boule, boule_dir)
        dessiner(joueur_d, joueur_g, boule)
        clock.tick(FPS)
 
    pygame.quit()
 
 
if __name__ == "__main__":
    main()