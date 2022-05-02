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
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                rect.left = 0
            if event.key == pygame.K_d:
                rect.right = LARGEUR
            if event.key == pygame.K_z:
                rect.top = 0
            if event.key == pygame.K_s:
                rect.bottom = HAUTEUR

            if event.key == pygame.K_c:
                rect.center = (LARGEUR/2, HAUTEUR/2)            
    dessiner()
    clock.tick(FPS)

pygame.quit()
