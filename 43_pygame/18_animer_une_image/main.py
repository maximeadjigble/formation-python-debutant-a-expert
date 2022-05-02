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

#Acteur 
acteur = pygame.image.load(os.path.join('assets', 'acteur_R0.png')).convert_alpha()
acteur_rect = acteur.get_rect()
acteur_rect = acteur_rect.inflate((-20,-5))
acteur_rect.midbottom = (LARGEUR/2, HAUTEUR)

#Pièces
piece_id = 0
pieces = [ pygame.image.load(os.path.join('assets', f'piece_{i}.png')).convert_alpha() for i in range(1,8)]
piece_rects = []
for i in range(5):
    piece_rects.append(pieces[0].get_rect(center = (200*i, HAUTEUR - 150)))

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
    fenetre.fill('white') 

    for p in piece_rects:
        # pygame.draw.rect(fenetre, '#F7D000', p)
        fenetre.blit(pieces[int(piece_id)], p)

    # pygame.draw.rect(fenetre, 'blue', acteur_rect)
    fenetre.blit(acteur, acteur.get_rect(center=acteur_rect.center))
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
        acteur_rect.x -= VITESSE_DEPLACEMENT
    if touches[pygame.K_d]:
        acteur_rect.x += VITESSE_DEPLACEMENT
    if touches[pygame.K_SPACE]:
        en_saut = True

    #Gestion du saut
    if en_saut:
        t_saut, fin_saut = sauter(acteur_rect, t_saut, VITESSE_SAUT, HAUTEUR_SAUT) 
        if fin_saut:
            en_saut = False
            t_saut = -math.sqrt(HAUTEUR_SAUT)

    #Gestion des collisions
    for i, p in enumerate(piece_rects):
        if acteur_rect.colliderect(piece_rects[i]):
            print(f"Collision avec {i}")       

    piece_id += 0.1
    if piece_id >= len(pieces):
        piece_id = 0

    dessiner()
    clock.tick(FPS)
 
pygame.quit()