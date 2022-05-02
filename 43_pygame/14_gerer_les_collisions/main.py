import pygame
import math
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Mon jeu PyGame')
FPS = 60 
VITESSE_DEPLACEMENT = 5
VITESSE_SAUT = 0.5
HAUTEUR_SAUT = 100
t_saut = -math.sqrt(HAUTEUR_SAUT)
en_saut = False

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
    fenetre.fill('white') 

    for p in pieces:
        pygame.draw.rect(fenetre, '#F7D000', p)

    pygame.draw.rect(fenetre, 'blue', rect)
    pygame.display.update()
 
executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False
 
    touches = pygame.key.get_pressed()
    if touches[pygame.K_q]:
        rect.x -= VITESSE_DEPLACEMENT
    if touches[pygame.K_d]:
        rect.x += VITESSE_DEPLACEMENT
    if touches[pygame.K_SPACE]:
        en_saut = True

    if en_saut:
        t_saut, fin_saut = sauter(rect, t_saut, VITESSE_SAUT, HAUTEUR_SAUT) 
        if fin_saut:
            en_saut = False
            t_saut = -math.sqrt(HAUTEUR_SAUT)

    # if rect.colliderect(pieces[1]):
    #     print("Collision")
    for i, p in enumerate(pieces):
        if rect.colliderect(pieces[i]):
            print(f"Collision avec {i}")       

    dessiner()
    clock.tick(FPS)
 
pygame.quit()