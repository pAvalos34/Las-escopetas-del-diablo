"""
Dust in the barrel, by Lonely Pug
Code by Pablo Avalos
2015-07-11

Juego de exploracion con godview, pistolas y animalitos
"""
import pygame, sys
from pygame.locals import *

#Paleta de colores
class color:
	Tiffany = (0, 146, 188)
	Morado = (97, 6, 188)
	Rosa = (233, 68, 168)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Dust in the barrel") #Titulo de la ventana
Walbert = pygame.image.load("Img/Walbert.png")
rectangulo1 = pygame.Rect(0,0,100,50)

def Main():
	PosX, PosY = 50, 100 #Posicion inicial
	Vel = 20 #Velocidad de Movimiento

	while True: #Loop para iniciar el juego
		screen.fill(color.Tiffany) #Fondo
		screen.blit(Walbert, (PosX, PosY)) #Posicion del personaje
		rectangulo1.left, rectangulo1.top = pygame.mouse.get_pos() #Mouse mueve reactangulo
		pygame.draw.rect(screen,color.Rosa,rectangulo1)

		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			#Movimiento con flechas de teclado
			elif event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					PosX -= Vel
				elif event.key == K_RIGHT:
					PosX += Vel
				elif event.key == K_UP:
					PosY -= Vel
				elif event.key == K_DOWN:
					PosY += Vel

		pygame.display.update()

Main()
