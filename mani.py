#import libreries 
import pygame
from pygame.locals import *
import constantes
import time

class Snake():
    
    def __init__(self, padre_window):
        self.padre_window = padre_window
        self.snake332 = pygame.image.load("imagenes\segmented-circle-arrow.png")
        self.x = 100
        self.y = 100
        self.direccion = "right"

    def draw(self):
        self.padre_window.fill(constantes.Color)
        self.padre_window.blit(self.snake332, (self.x, self.y))
        pygame.display.flip()

    def move_left(self):
        self.direccion = "left"

    def move_right(self):
        self.direccion = "right"

    def move_up(self):
        self.direccion = "up"

    def move_dawn(self):
        self.direccion = "down"

    def walk(self):
        if self.direccion == "left":
            self.x -= 10

        if self.direccion == "right":
            self.x += 10
        
        if self.direccion == "up":
            self.y -= 10
        
        if self.direccion == "down":
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

            self.snake.walk()
            time.sleep(0.1)


game = Game()
game.run()


