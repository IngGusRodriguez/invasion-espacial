import pygame
import random
import math

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
enemigoimg = []
enemigox = []
enemigoy = []
enemigox_cambio = []
enemigoy_cambio = []
cantidad_enemigos = 8

for e in range(cantidad_enemigos):
    enemigoimg.append(pygame.image.load("enemigo.png"))
    enemigox.append(random.randint(0, 736))
    enemigoy.append(random.randint(50, 200))
    enemigox_cambio.append(0.5)
    enemigoy_cambio.append(50)

#Variables de la bala
balaimg = pygame.image.load("bala.png")
balax = 0
balay = 500
balax_cambio = 0
balay_cambio = 3
bala_visible = False

# Variable puntaje
puntaje = 0

#Función jugador
def jugador(x, y):
    pantalla.blit(jugadorimg, (x, y))

#Función enemigo
def enemigo(x, y, ene):
    pantalla.blit(enemigoimg[ene], (x, y))

#Función bala
def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(balaimg, (x + 16, y + 10))

#Función para detectar colisiones
def hay_colision(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y2 - y1, 2))
    if distancia < 27:
        return True
    else:
        return False

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
            if evento.key == pygame.K_SPACE:
                if not bala_visible:
                   balax = jugadorx
                   disparar_bala(balax, balay)

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
    for e in range(cantidad_enemigos):
        enemigox[e] += enemigox_cambio[e]

    #Mantener dentro de margenes al enemigo
        if enemigox[e] <= 0:
            enemigox_cambio[e] = 1
            enemigoy[e] += enemigoy_cambio[e]
        elif enemigox[e] >= 736:
            enemigox_cambio[e] = -1
            enemigoy[e] += enemigoy_cambio[e]

    #Colisión
        colision = hay_colision(enemigox[e], enemigoy[e], balax, balay)
        if colision:
            balay = 500
            bala_visible = False
            puntaje += 1
            print(puntaje)
            enemigox[e] = random.randint(0, 736)
            enemigoy[e] = random.randint(50, 200)

        enemigo(enemigox[e], enemigoy[e], e)



    #Movimiento bala
    if balay <= -64:
        balay = 500
        bala_visible = False

    if bala_visible:
        disparar_bala(balax, balay)
        balay -= balay_cambio


    jugador(jugadorx, jugadory)


    #Actualizar
    pygame.display.update()

