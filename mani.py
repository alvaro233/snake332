#git status
#git add .
# git commit -m "mensaje"
# #import libreries 
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

    def move(self):
        self.x = random.randint(24,776)
        self.y = random.randint(24,576)
    

        

class Snake():
    
    def __init__(self, padre_window,lenght):
        self.padre_window = padre_window
        self.snake332 = pygame.image.load("imagenes\segmented-circle-arrow.png")
       
        self.direccion = "right"
        self.lenght = lenght
        self.x = [24]*lenght
        self.y = [24]*lenght

    #serpiente crese
    def increase_lenght(self):
        self.lenght += 1
        self.x.append(-1)
        self.y.append(-1)


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
            self.x[0] -= 24

        if self.direccion == "right":
            self.x[0] += 24
        
        if self.direccion == "up":
            self.y[0] -= 24
        
        if self.direccion == "down":
            self.y[0] += 24

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
    
    def is_colicion(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + constantes.Snake_body:
           if y1 >= y2 and y1 < y2 + constantes.Snake_body: 
            return True
        return False
        
    
    def play(self):
        self.snake.walk()
        self.orange.draw()
        self.display_score()
        pygame.display.flip()

        if self.is_colicion(self.snake.x[0], self.snake.y[0], self.orange.x, self.orange.y):
            self.snake.increase_lenght()
            self.orange.move()

        #cuerpo

        for B in range(2, self.snake.lenght):
            if self.is_colicion(self.snake.x[0], self.snake.y[0], self.snake.x[B], self.snake.y[B]):
                print("Game over")
                self.show_game_over()

        def show_game_over(self):
            font = pygame.font.Font("imagene/texto ...otf")
            message1 = font.render(f"Game Over!! comeste:{self.lenght}", True, ("#black"))
            self.window.blit(message1, (400, 300))
            message2 = font.render(f"Juega otra ves pulsando ENTER o salte pulsando ESC", True, ("#black"))
            self.window.blit(message2, (400, 335))
            pygame.display.flip()


        #if self.is_colicion == False:
            #constantes.Velocidad == 0.01


        #score
    def display_score(self):
        font = pygame.font.Font("imagenes/texto ...otf", 30)
        score = font.render(f"Puntos:{self.snake.lenght -3}", True,("red"))
        self.Ventana.blit(score, (15, 15))
    

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

            self.play()

            time.sleep(0.1)


game = Game()
game.run()


