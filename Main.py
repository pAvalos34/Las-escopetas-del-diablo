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
	Pantone_C = (0, 146, 188)

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Dust in the barrel")
Walbert = pygame.image.load("Img/Walbert.png")


def Main():
	PosX = 50
	PosY = 100
	Vel = 20
	
	while True:
		screen.fill(color.Pantone_C)
		screen.blit(Walbert, (PosX, PosY))
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == K_LEFT:
					PosX =  PosX - Vel
				elif event.key == K_RIGHT:
					PosX = PosX + Vel
				elif event.key == K_UP:
					PosY = PosY - Vel
				elif event.key == K_DOWN:
					PosY = PosY + Vel
								
		pygame.display.update()

Main()
