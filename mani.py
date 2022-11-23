#import libreries 
import pygame
from pygame.locals import *
import constantes

class Game():
    def __init__(self):
        pygame.init()
        self.Ventana = pygame.display.set_mode(constantes.Ventana)
        self.title = pygame.display.set_caption(constantes.Title)
        Icono = pygame.image.load("imagenes\snake.png")
        pygame.display.set_icon(Icono)
        self.Ventana.fill(constantes.Color)
        pygame.display.update()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                elif event.type == QUIT:
                    running = False 


game = Game()
game.run()


