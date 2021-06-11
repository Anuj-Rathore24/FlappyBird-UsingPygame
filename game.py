import pygame
import time
import random
from tkinter import *

pygame.init()

display_width=800
display_height=600

gamedisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("Flappy Bird")


green = (0,255,0)
blue = (102,184,252)
poles_color=(235,255,3)
poles2_color=(254,200,8)
poles_ychange=2
poles_xchange=2

clock=pygame.time.Clock()
crashed=False
birdimg=pygame.image.load("bird2.png")
cloudimg=pygame.image.load("clouds.png")
poles=pygame.image.load("poles.png")

def bird(x,y):
    gamedisplay.blit(birdimg,(x,y))
def clouds(x,y):
    gamedisplay.blit(cloudimg,(x,y))


x=(display_width*0.3)
y=(display_height*0.8)
y_change=0
poles_y=750
poles_x=random.randint(0,540)
second_poles_y=950
second_poles_x=random.randint(0,540)
third_poles_y=1150
third_poles_x=random.randint(0,540)

points=0

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y_change=10
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                y_change=0
    y=y-y_change
    if y<550:
        y=y+5
    
        
    pygame.draw.rect(gamedisplay,blue,(0,0,800,350),0 )
    pygame.draw.rect(gamedisplay,green,(0,350,800,250),0 )
    clouds(0,100)
    bird(x,y)
    
    def poles(x,y):
      global poles_y
      global poles_x
      pygame.draw.rect(gamedisplay,poles_color,(y,0,50,x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x,55,10),0 )
      pygame.draw.rect(gamedisplay,poles_color,(y,x+150,50,600-x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x+140,55,10),0 )
      if y==-50:
          poles_y=800
          poles_x=random.randint(0,540)
    
    
    def second_poles(x,y):
      global second_poles_y
      global second_poles_x
      pygame.draw.rect(gamedisplay,poles_color,(y,0,50,x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x,55,10),0 )
      pygame.draw.rect(gamedisplay,poles_color,(y,x+150,50,600-x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x+140,55,10),0 )
      if y==-50:
          second_poles_y=800
          second_poles_x=random.randint(0,540)
    
    def third_poles(x,y):
      global third_poles_y
      global third_poles_x
      pygame.draw.rect(gamedisplay,poles_color,(y,0,50,x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x,55,10),0 )
      pygame.draw.rect(gamedisplay,poles_color,(y,x+150,50,600-x),0 )
      pygame.draw.rect(gamedisplay,poles2_color,(y-2.5,x+140,55,10),0 )
      if y==-50:
          third_poles_y=800
          third_poles_x=random.randint(0,540)
    
    
    poles(poles_x,poles_y)
    second_poles(second_poles_x,second_poles_y)        
    third_poles(third_poles_x,third_poles_y)        
    
    poles_y=poles_y-poles_ychange
    second_poles_y=second_poles_y-poles_ychange
    third_poles_y=third_poles_y-poles_ychange
      
    if x == poles_y  or x==poles_y+50:
        if y < poles_x +10 or y>poles_x+140:
            crashed=True
        else:
            points=points+1 
    if x == second_poles_y  or x==second_poles_y+50:
        if y < second_poles_x +10 or y>second_poles_x +140:
            crashed=True
        else:
            points=points+1 
    if x == third_poles_y or x==third_poles_y+50:
        if y < third_poles_x +10 or y>third_poles_x+140:
            crashed=True
        else:
            points=points+1 
    
    
    pygame.display.update()
    clock.tick(60)



window=Tk()
window.title("Points table")
label1=Label(window, text="Your Score Is...",padx=10, pady=10,)
label1.pack()
label2=Label(window,text=str(points),padx=10, pady=10,)
label2.pack()
window.mainloop()
pygame.quit()
quit()
