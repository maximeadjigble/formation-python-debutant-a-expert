import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))

FPS = 60
 
def dessiner():
    fenetre.fill('white') 
    pygame.display.update()

debuter = False
executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False 
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                debuter = True
                print("Bouton Gauche")
            if event.button == pygame.BUTTON_RIGHT:
                print("Bouton Droit")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                debuter = False
                print("Bouton Gauche relaché")

        if event.type == pygame.MOUSEMOTION and debuter:
            print("Déssiner")

    dessiner()
    clock.tick(FPS)
 
pygame.quit()