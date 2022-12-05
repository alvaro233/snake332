#import libreries 
import pygame
from pygame.locals import *
import constantes
import time
import random

class orange():
    def __init__(self, padre_window):
        self.padre_window = padre_window
        self.image = pygame.image.load("imagenes\orange.png")
        self.x = 120
        self.y = 120

    def draw(self):
        self.padre_window.blit(self.image, (self.x, self.y))
        pygame.display.flip()

        

class Snake():
    
    def __init__(self, padre_window,lenght):
        self.padre_window = padre_window
        self.snake332 = pygame.image.load("imagenes\segmented-circle-arrow.png")
       
        self.direccion = "right"
        self.lenght = lenght
        self.x = [24]*lenght
        self.y = [24]*lenght


    def draw(self):
        
        self.padre_window.fill(constantes.Color)
        for A in range(self.lenght):
            self.padre_window.blit(self.snake332, (self.x[A], self.y[A]))
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
        # update body
        for A in range(self.lenght-1, 0, -1):
            self.x[A] = self.x[A-1]
            self.y[A] = self.y[A-1]

            # updite head 
        if self.direccion == "left":
            self.x[0] -= 10

        if self.direccion == "right":
            self.x[0] += 10
        
        if self.direccion == "up":
            self.y[0] -= 10
        
        if self.direccion == "down":
            self.y[0] += 10

        self.draw()

class Game():
    def __init__(self):
        pygame.init()
        self.Ventana = pygame.display.set_mode(constantes.Ventana)
        self.title = pygame.display.set_caption(constantes.Title)
        Icono = pygame.image.load("imagenes\snake.png")
        pygame.display.set_icon(Icono)
        self.Ventana.fill(constantes.Color)
        self.snake = Snake(self.Ventana, 3)
        self.snake.draw()
        self.orange = orange(self.Ventana)
        self.orange.draw()
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
            self.orange.draw
            time.sleep(0.1)


game = Game()
game.run()


