import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

FPS = 60

def dessiner(couleur):
    fenetre.fill(couleur)
    pygame.display.update()

executer = True
couleur = (255,255,255)
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos[0], event.pos[1]
            # print("x", x/LARGEUR, "y", y/HAUTEUR)
            couleur = (int(255*x/LARGEUR), int(255*y/HAUTEUR), 255)
            
    dessiner(couleur)
    clock.tick(FPS)

pygame.quit()
