import pygame
import time

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

FPS = 60

executer = True
clock = pygame.time.Clock()
while executer:
    t1 = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False

    fenetre.fill('white')
    pygame.display.update()
    clock.tick(FPS)
    print("Durée (s):", time.time() - t1)

pygame.quit()