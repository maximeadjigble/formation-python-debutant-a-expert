import pygame

pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Mon jeu PyGame")

FPS = 60

def dessiner():
    fenetre.fill('white')
    #Rectangle 
    pygame.draw.rect(fenetre, 'red', (0,30,80, 120))

    #Cercle
    pygame.draw.circle(fenetre, 'blue', (100,200), 40)

    #Ellipse
    pygame.draw.ellipse(fenetre, 'green', (300, 200, 200, 100),4)
    
    #Ligne
    pygame.draw.line(fenetre, 'red', (550, 80), (650,300),4)

    #Polygone
    pygame.draw.polygon(fenetre, 'black', [(250, 100), (300,80), (500,150), (500,100)], 4)
    pygame.display.update()

executer = True
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False

    dessiner()
    clock.tick(FPS)

pygame.quit()