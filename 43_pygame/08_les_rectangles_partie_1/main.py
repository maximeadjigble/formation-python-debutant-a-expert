import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

FPS = 60

rect = pygame.Rect(40,20,200,100)

def dessiner():
    fenetre.fill('white')
    pygame.draw.rect(fenetre, 'blue', rect)
    pygame.display.update()

executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False

    # rect.x += 1
    # rect.y += 4
    # rect.w += 1
    rect.h += 1
    dessiner()
    clock.tick(FPS)

pygame.quit()
