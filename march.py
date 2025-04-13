import pygame
from random import randint
pygame.init()
screen=pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.update()
Iron_man=pygame.image.load("iron_man.jpeg")
thor=pygame.image.load("thor.jpeg")
#thor = pygame.transform.scale(ludo,(100,100))
Black_widow=pygame.image.load("black_widow.jpeg")
spiderman=pygame.image.load("spideman.jpeg")
screen.blit(Iron_man,(150,100))
screen.blit(thor,(150,200))
screen.blit(Black_widow,(150,300))
screen.blit(spiderman,(150,400))
font=pygame.font.SysFont("Times New Roman", 36)
text=font.render("Black_widow", True,(0,0,0))
text1=font.render("Iron_man", True,(0,0,0))
text2=font.render("spiderman", True,(0,0,0))
text3=font.render("thor", True,(0,0,0))
screen.blit(text,(350,100))
screen.blit(text1,(350,200))
screen.blit(text2,(350,300))
screen.blit(text3,(350,400))
pygame.display.update()
r=randint(0,255)
g=randint(0,255)
b=randint(0,255)
clr=(r,g,b)
while 1:

    event = pygame.event.poll()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # if it is quit the game
            pygame.quit()
            exit(0)
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(screen,
         ((clr)) ,(pos), 20, 0)
        pygame. display.update()
    elif event.type == pygame.MOUSEBUTTONUP:
        pos2 = pygame.mouse.get_pos()
        pygame.draw.line(screen, ((clr)), (pos), (pos2),5)
        pygame.draw.circle(screen,
        ((clr)) ,(pos2), 20, 0)
        pygame.display.update()
