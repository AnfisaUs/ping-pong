# main.py 
import pygame    
pygame.init() 
from pygame.sprite import Sprite
from config import *
from ract import Ract    
from circle import Circle 

def move_bot(): 
        if circle1.rect.centery > ract1.rect.centery and circle1.rect.centerx < WIDTH/2: 
            ract1.rect.y -= y_speed      
        if circle1.rect.centery < ract1.rect.centery and circle1.rect.centerx < WIDTH/2: 
            ract1.rect.y += y_speed       

sc = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption('пинг понг')  
clock = pygame.time.Clock() 

ract1 = Ract(10, 100)
ract2 = Ract(580, 100)      
circle1 = Circle(300, 150, 20)    
  
while True:  
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit() 
        ract1.on_event(event) 
        ract2.on_event(event)   
    move_bot() 
    sc.fill(GREY)  
    pygame.draw.rect(sc, BLACK, (0, 0, WIDTH, HEIGHT), 10)  
    pygame.draw.line(sc, BLACK, (300, 0), (300, 400), 5)   
    
    ract1.update() 
    ract2.update_second() 
    circle1.update(ract1, ract2) 
    ract1.draw(sc) 
    ract2.draw(sc)
    circle1.draw_circle(sc)  
    clock.tick(FPS)   
    pygame.display.update()

