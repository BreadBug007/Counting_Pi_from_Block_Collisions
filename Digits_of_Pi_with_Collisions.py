import pygame
from pygame.locals import *
from Blocks import Block


def main():
    
    pygame.init()
    
    screen = pygame.display.set_mode((800,600))
    
    pygame.display.set_caption("Colliding Blocks")
    
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    
    timesteps = 10000
    digits = 5
    
    
    block1 = Block()
    block1.x, block1.y = 300, 575
    block1.w = 25
    block1.v_x, block1.m = 0, 1
    block1.xmin, block1.xmax = 0, 10000
    block2 = Block()
    block2.x, block2.y = 500, 450
    block2.w = 150
    block2.v_x, block2.m = -1/timesteps, pow(100,digits-1)
    block2.xmin, block2.xmax = 25, 10000
    
    myfont = pygame.font.SysFont('monospace', 40)
    
    count = 0
    
    while True:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:            
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == ord('q'):
                    pygame.quit()
        
        screen.fill(BLACK)
        
        text = myfont.render("Count:" + str(count), 1, (0, 0, 255))
        screen.blit(text, (300, 200))    
        
        for i in range(timesteps):
            if block1.collide(block2):
                 v1 = block1.bounce(block2)
                 v2 = block2.bounce(block1)
                 block1.v_x = v1
                 block2.v_x = v2
                 count += 1
            
            if block1.wall_collide():
                count += 1
                block1.reverse()
            
            block1.move()
            block2.move()
        
        block1.show(screen, (255, 0, 0))
        block2.show(screen, (0, 255, 0))
        
        pygame.display.update()
        
main()