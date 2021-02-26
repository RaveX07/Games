import pygame
import os

pygame.init()

#colors
WHITE = (255,255,255)

#variables
status = 0

#load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

#setup display
win = pygame.display.set_mode((800, 500))
win.fill(WHITE)
pygame.display.set_caption("Game by Jannis")

def draw():
    rect = images[status].get_rect()
    win.blit(images[status], rect)


#setup game loop
FPS = 60
clock = pygame.time.Clock()
clock.tick(FPS)

#loop
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
    draw()


