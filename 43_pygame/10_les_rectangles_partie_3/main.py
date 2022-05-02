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
            if event.key == pygame.K_c:
                rect.center = (LARGEUR/2, HAUTEUR/2)            
    
    touches = pygame.key.get_pressed()
    if touches[pygame.K_d]:
        rect.x += 5
    if touches[pygame.K_q]:
        rect.x -= 5
    if touches[pygame.K_z]:
        rect.y -= 1
    if touches[pygame.K_s]:
        rect.y += 1
    dessiner()
    clock.tick(FPS)

pygame.quit()
