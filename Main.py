""" Dust in the barrel, by Lonely Pug
	Code by Pablo Avalos
	2015-07-11

	Juego de exploracion con godview, pistolas y animalitos """

import pygame, sys
from pygame.locals import *

def Main():
	print "Hola"
	print "Tengo un numero entre 1 y 100"
	Respuesta = False #Flag para identificar 
	Num = 34 #Numero de la computadora

	while not Respuesta:
		NumUsu = input ("Dime cual es:	")
		if NumUsu == Num:
			print "Ese era"
			Respuesta = True
		else:
			print "Tenemos toda el tiempo del mundo, soy de 64 bits"

Main()
