import pygame
import sys
 
pygame.init()
LARGEUR, HAUTEUR = 800, 400
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption('Clone Paint')
pygame.display.set_icon(pygame.image.load('favicon.png'))

FPS = 60
 
def dessiner():
    fenetre.fill('white') 
    pygame.display.update()

def main():
    debuter = False
    executer = True
    clock = pygame.time.Clock()
    while executer:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executer = False 
                pygame.quit()
                sys.exit()
        
        dessiner()
        clock.tick(FPS)
    
if __name__ == "__main__":
    main()