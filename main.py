import pygame
import random

pygame.init()

#pantalla
pantalla = pygame.display.set_mode((800, 600))

#Título e Icono
pygame.display.set_caption("Invasión Espacial")
icono = pygame.image.load("ovni.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo.jpg")

#Variables del jugador
jugadorimg = pygame.image.load("cohete.png")
jugadorx = 368
jugadory = 500
jugadorx_cambio = 0

#Variables del enemigo
enemigoimg = pygame.image.load("enemigo.png")
enemigox = random.randint(0, 736)
enemigoy = random.randint(50, 200)
enemigox_cambio = 1
enemigoy_cambio = 50

#Función jugador
def jugador(x, y):
    pantalla.blit(jugadorimg, (x, y))

#Función enemigo
def enemigo(x, y):
    pantalla.blit(enemigoimg, (x, y))

#Loop
ejecucion = True
while ejecucion:

    #Imagen de fondo
    pantalla.blit(fondo, (0, 0))

    #Evento cerrar
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecucion = False

        #Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio = -1
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio = +1

        #Evento soltar teclas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorx_cambio = 0

    #Modificar ubicación del jugador
    jugadorx += jugadorx_cambio

    #Mantener dentro de margenes al jugador
    if jugadorx <=0:
        jugadorx = 0
    elif jugadorx >= 736:
        jugadorx = 736

    # Modificar ubicación del enemigo
    enemigox += enemigox_cambio

    # Mantener dentro de margenes al enemigo
    if enemigox <= 0:
        enemigox_cambio = 1
        enemigoy += enemigoy_cambio

    elif enemigox >= 736:
        enemigox_cambio = -1
        enemigoy += enemigoy_cambio




    jugador(jugadorx, jugadory)
    enemigo(enemigox, enemigoy)

    #Actualizar
    pygame.display.update()

