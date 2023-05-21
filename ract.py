# ract.py 
import pygame 
pygame.init() 
from pygame.sprite import Sprite
from config import *

class Ract(Sprite): 
    def __init__(self, x, y):  
        super().__init__()
        self.rect = pygame.Rect(x, y, 10, RACT_HEIGHT)  
        self.image = pygame.Surface((10, RACT_HEIGHT)) 
        self.image.fill(BLUE) 
        self.moving_up = False
        self.moving_down = False    
    
    def on_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: 
                self.moving_up = True 
            elif event.key == pygame.K_DOWN:  
                self.moving_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP: 
                self.moving_up = False 
            elif event.key == pygame.K_DOWN: 
                self.moving_down = False 
           
    def update(self):
        if self.rect.y > HEIGHT - 110 :   
            self.rect.y = 290  
        if self.rect.y < 10 : 
            self.rect.y = 10  
       
    def update_second(self): 
        if self.moving_up:
            self.rect.move_ip(0, -5) 
        if self.moving_down: 
            self.rect.move_ip(0, 5) 
        if self.rect.bottom > HEIGHT - 10:   
            self.rect.bottom = HEIGHT - 10    
        if self.rect.top < 10: 
            self.rect.top = 10             

    def draw(self, surface):
        surface.blit(self.image, self.rect) 



        