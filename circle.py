# circle.py 
import pygame 
pygame.init() 
from pygame.sprite import Sprite
from config import *
from ract import * 

class Circle(Sprite): 
    def __init__(self, x, y, r): 
        self.x_speed = x_speed  
        self.y_speed = y_speed 
        super().__init__() 
        d = 2*r   
        self.rect = pygame.Rect(x, y, d, d)  
        self.image = pygame.Surface((d, d), pygame.SRCALPHA, 32)   
        self.image = self.image.convert_alpha()
        pygame.draw.circle(self.image, YELLOW, (r, r), r)                            

    def draw_circle(self, wind):   
        wind.blit(self.image, self.rect) 

    def update(self, ract1, ract2):
        global x_speed 
        global y_speed

        self.rect.move_ip(self.x_speed, self.y_speed) 

        if self.rect.bottom > HEIGHT - 10:
            self.rect.bottom = HEIGHT - 10
            self.y_speed = -self.y_speed 
        if self.rect.top < 10: 
            self.rect.top = 10
            self.y_speed = -self.y_speed 

        # При столкновении с игроком
        if ract2.rect.colliderect(self.rect):
            self.rect.right = ract2.rect.left
            self.x_speed = -self.x_speed 

        # При столкнвоении с ботом
        elif ract1.rect.colliderect(self.rect): 
            self.rect.left = ract1.rect.right
            self.x_speed = -self.x_speed

        # Возвращаем в обратную позицию
        elif self.rect.x > 590: 
            self.rect.x = 300
            self.rect.y = 150 
        elif self.rect.x < 10: 
            self.rect.x = 300
            self.rect.y = 150 





            