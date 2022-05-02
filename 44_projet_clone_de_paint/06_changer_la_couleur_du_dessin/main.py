import pygame
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))

FPS = 60
palette_rect = []
palette_couleurs = ['black', 'red', 'green', 'blue', 'violet']
for i in range(len(palette_couleurs)):
    palette_rect.append(pygame.Rect(5+20*i,5,20,20))

def dessiner(points, couleurs):
    fenetre.fill('white') 

    for k, _points in enumerate(points):
        if len(_points) >= 2:
            for i, p in enumerate(_points):
                if i+1 >= len(_points):
                    break
                pygame.draw.line(fenetre, couleurs[k], p, _points[i+1], 4)
    
    for i, rect in enumerate(palette_rect):
        pygame.draw.rect(fenetre, palette_couleurs[i], rect)
    pygame.display.update()

debuter = False
executer = True
points = []
couleur = 'black'
couleurs = []
clock = pygame.time.Clock()
while executer:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executer = False 
      
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                activer_dessin = True
                for i, rect in enumerate(palette_rect):
                    if rect.collidepoint(event.pos):
                        activer_dessin = False
                        couleur = palette_couleurs[i]
                        
                if activer_dessin:
                    debuter = True
                    points.append([]) 
                    couleurs.append(couleur)
                    # print(couleurs, len(points))

            if event.button == pygame.BUTTON_RIGHT:
                points = []
                couleurs = []

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == pygame.BUTTON_LEFT:
                debuter = False

        if event.type == pygame.MOUSEMOTION and debuter:
            points[-1].append(event.pos)

    dessiner(points, couleurs)
    clock.tick(FPS)
 
pygame.quit()