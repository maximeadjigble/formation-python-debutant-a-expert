import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

executer = True
while executer:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            executer = False


pygame.quit()