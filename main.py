import pygame
pygame.init()

pygame.display.set_caption(".")
screen = pygame.display.set_mode((1080, 620))

run = True
background = pygame.image.load('JEU PYTHON/téléchargement.jpg')

while run:

    screen.blit(background, (440, 200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            print("Quitting")


