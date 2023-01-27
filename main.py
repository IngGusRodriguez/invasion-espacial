import pygame
pygame.init()

#pantalla
pantalla = pygame.display.set_mode((800, 600))

#Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)

#Variables del jugador
jugadorimg = pygame.image.load("cohete.png")
jugadorx = 368
jugadory = 536
jugadorx_cambio = 0
jugadory_cambio = 0;

#Función jugador
def jugador(x, y):
    pantalla.blit(jugadorimg, (x, y))

#Loop
ejecucion = True
while ejecucion:

    #RGB
    pantalla.fill((205, 144, 228))

    #Evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecucion = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio = +0.3

        #Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0

    #Modificar ubicación
    jugadorx += jugadorx_cambio

    #Mantener dentro de margenes
    if jugadorx <=0:
        jugadorx = 0
    elif jugadorx >= 736:
        jugadorx = 736


    jugador(jugadorx, jugadory)

    #Actualizar
    pygame.display.update()

