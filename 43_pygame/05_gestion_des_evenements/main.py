import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

FPS = 60

def dessiner():
    fenetre.fill('white')
    pygame.display.update()

executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            executer = False
        # if event.type == pygame.MOUSEMOTION:
        #     pass
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("ESPACE")
            if event.key == pygame.K_a:
                print("A")
        # if event.type == pygame.KEYUP:
        #     print("Up", event)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                print("Gauche")
            if event.button == pygame.BUTTON_RIGHT:
                print("Droit")



    dessiner()
    clock.tick(FPS)

pygame.quit()