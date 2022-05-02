import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))

FPS = 60
 
def dessiner(points):
    fenetre.fill('white') 

    if len(points) >= 2:
        for i, p in enumerate(points):
            if i+1 >= len(points):
                break
            pygame.draw.line(fenetre, 'black', p, points[i+1], 4)
    pygame.display.update()

debuter = False
executer = True
points = []
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False 
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                debuter = True

            if event.button == pygame.BUTTON_RIGHT:
                print("Bouton Droit")

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                debuter = False
                points = []

        if event.type == pygame.MOUSEMOTION and debuter:
            # print(event.pos)
            points.append(event.pos)

    dessiner(points)
    clock.tick(FPS)
 
pygame.quit()