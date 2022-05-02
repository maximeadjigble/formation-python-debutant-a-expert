import os
import pygame
import math
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Mon jeu PyGame')
pygame.display.set_icon(pygame.image.load('favicon.png'))

#Parametres
FPS = 60 
VITESSE_DEPLACEMENT = 5
VITESSE_SAUT = 0.5
HAUTEUR_SAUT = 100
t_saut = -math.sqrt(HAUTEUR_SAUT)
en_saut = False

#Acteur & Pièces
acteur = pygame.image.load(os.path.join('assets', 'acteur_R0.png')).convert_alpha()
acteur = pygame.transform.scale(acteur, (200,200))
rect = pygame.Rect(LARGEUR/2-15,HAUTEUR-50,30,50)
pieces = []
for i in range(5):
    pieces.append(pygame.Rect(200*i, HAUTEUR - 150, 20, 20))

def sauter(rect, t, vitesse, hauteur):
    y_initiale = HAUTEUR - rect.h
    t += vitesse
    fin_saut = False
    rect.y = y_initiale - (hauteur - t**2)
    if rect.y >= y_initiale:
        fin_saut = True
        rect.y = y_initiale
    return t,fin_saut 

def dessiner():
    fenetre.fill('gray') 

    for p in pieces:
        pygame.draw.rect(fenetre, '#F7D000', p)

    fenetre.blit(acteur, (0,0))
    pygame.draw.rect(fenetre, 'blue', rect)
    pygame.display.update()

#Boucle principale
executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False
    
    #Gestion des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q]:
        rect.x -= VITESSE_DEPLACEMENT
    if touches[pygame.K_d]:
        rect.x += VITESSE_DEPLACEMENT
    if touches[pygame.K_SPACE]:
        en_saut = True

    #Gestion du saut
    if en_saut:
        t_saut, fin_saut = sauter(rect, t_saut, VITESSE_SAUT, HAUTEUR_SAUT) 
        if fin_saut:
            en_saut = False
            t_saut = -math.sqrt(HAUTEUR_SAUT)

    #Gestion des collisions
    for i, p in enumerate(pieces):
        if rect.colliderect(pieces[i]):
            print(f"Collision avec {i}")       

    dessiner()
    clock.tick(FPS)
 
pygame.quit()