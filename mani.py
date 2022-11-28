#import libreries 
import pygame
from pygame.locals import *
import constantes

class Snake():
    
    def __init__(self, padre_window):
        self.padre_window = padre_window
        self.snake332 = pygame.image.load("imagenes\segmented-circle-arrow.png")
        self.x = 100
        self.y = 100

    def draw(self):
        self.padre_window.fill(constantes.Color)
        self.padre_window.blit(self.snake332, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.x -= 10
        self.draw()

    def move_right(self):
        self.x += 10    
        self.draw()

    def move_up(self):
        self.y -= 10
        self.draw()

    def move_dawn(self):
        self.y += 10
        self.draw()
        


class Game():
    def __init__(self):
        pygame.init()
        self.Ventana = pygame.display.set_mode(constantes.Ventana)
        self.title = pygame.display.set_caption(constantes.Title)
        Icono = pygame.image.load("imagenes\snake.png")
        pygame.display.set_icon(Icono)
        self.Ventana.fill(constantes.Color)
        self.snake = Snake(self.Ventana)
        self.snake.draw()
        pygame.display.update()

    def run(self): 
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key == K_RIGHT:
                        self.snake.move_right()

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_dawn()

                elif event.type == QUIT:
                    running = False 


game = Game()
game.run()


