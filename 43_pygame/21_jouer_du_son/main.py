import os
import pygame
import math
 
pygame.init()
# https://www.pygame.org/docs/ref/mixer.html
# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.mixer.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Mon jeu PyGame')
pygame.display.set_icon(pygame.image.load('favicon.png'))

#Parametres
FPS = 60 
VITESSE_DEPLACEMENT = 5
VITESSE_SAUT = 0.5
HAUTEUR_SAUT = 100
VITESSE_ANIMATION_ACTEUR = 0.25
t_saut = -math.sqrt(HAUTEUR_SAUT)
en_saut = False

#Son
son_saut = pygame.mixer.Sound(os.path.join('assets', 'saut.wav'))
son_piece = pygame.mixer.Sound(os.path.join('assets', 'piece.wav'))
collision_id = 0

#Acteur 
acteur_id_right = 0
acteur_id_left = 0
acteur_right = [pygame.image.load(os.path.join('assets', f'acteur_R{i}.png')).convert_alpha() for i in range(0,4)]
acteur_left = [pygame.image.load(os.path.join('assets', f'acteur_L{i}.png')).convert_alpha() for i in range(0,4)]
acteur = acteur_right[0]

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                acteur = acteur_right[0]
                acteur_id_right = 1
            if event.key == pygame.K_q:
                acteur = acteur_left[0]
                acteur_id_left = 1

    #Gestion des touches
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q]:
        acteur_rect.x -= VITESSE_DEPLACEMENT

        acteur_id_left += VITESSE_ANIMATION_ACTEUR
        if acteur_id_left >= len(acteur_left):
            acteur_id_left = 1
        acteur = acteur_left[int(acteur_id_left)]
    if touches[pygame.K_d]:
        acteur_rect.x += VITESSE_DEPLACEMENT

        acteur_id_right += VITESSE_ANIMATION_ACTEUR
        if acteur_id_right >= len(acteur_right):
            acteur_id_right = 1
        acteur = acteur_right[int(acteur_id_right)]
    if touches[pygame.K_SPACE]:
        if not en_saut:
            son_saut.play()
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
            if collision_id != i:
                son_piece.play()      
            collision_id = i
            
    piece_id += 0.1
    if piece_id >= len(pieces):
        piece_id = 0

    dessiner()
    clock.tick(FPS)
 
pygame.quit()

