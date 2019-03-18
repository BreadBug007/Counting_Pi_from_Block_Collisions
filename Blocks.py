import pygame

class Block():
    
    def __init__(self):
        
        self.x = 0
        self.y = 0
        self.w = 0
        self.v_x = 0
        self.v_y = 0
        self.m = 0
        self.xmin = 0
        self.xmax = 0
        screen = pygame.display.get_surface()
    

    def show(self, screen, color):
        if self.x <= self.xmin:
            return pygame.draw.rect(screen, color, [self.xmin, self.y, self.w, self.w])
        elif self.x >= self.xmax:
            return pygame.draw.rect(screen, color, [self.xmax, self.y, self.w, self.w])
        else:
            return pygame.draw.rect(screen, color, [self.x, self.y, self.w, self.w])
    def move(self):
        self.x += self.v_x
    
    def collide(self, other):
        return self.x + self.w >= other.x
    
    def bounce(self, other):
        V = ((self.m - other.m)/(self.m + other.m))*self.v_x + (2*other.m/(self.m + other.m))*other.v_x
        return V
    
    def wall_collide(self):
        return self.x <= 0
    
    def reverse(self):
        self.v_x *= -1
          
