import sys
 
import pygame
 
# initialize pygame
pygame.init()
print("yayay")
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
# Game loop.
running = True
while running:
    screen.fill((0, 0, 0))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
  
    # Update.
  
    # Draw.
  
    pygame.display.flip()
    fpsClock.tick(fps)

pygame.quit()