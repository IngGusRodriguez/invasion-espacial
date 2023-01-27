import pygame
pygame.init()

pantalla = pygame.display.set_mode((800, 600))

ejecucion = True
while ejecucion:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecucion = False

