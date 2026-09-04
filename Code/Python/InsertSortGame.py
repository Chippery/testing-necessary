import pygame
import random
import time
import math

pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
color = "white"
thickness = 0


class rectangles():
    def __init__(self, how_many):
        self.draw_rectangle = None
        self.how_many = how_many
        self.base = 10
        self.ceil = HEIGHT - 50
        self.multiple = 1
        self.rectwidth = WIDTH // self.how_many
        self.nums = [random.randrange(self.base // self.multiple, self.ceil // self.multiple) * self.multiple 
                     for _ in range(self.how_many)] # Get List of Random Nums for Heights
        self.rects = []

        # (screen, color, (X Pos, Y Pos, Width, Height))
        for i in range(self.how_many):
            self.rects.append(pygame.Rect(self.rectwidth * i, HEIGHT - self.nums[i], self.rectwidth, self.nums[i]))

    def draw(self): # generate static rectangles once
        screen.fill("black")
        for r in range(len(self.rects)): # Iterate list of Rects & draw each w/Coordinates at r
            self.draw_rectangle = pygame.draw.rect(screen, color, self.rects[r], thickness)
        pygame.display.flip()
    
    def sort_rects(self): # Compare Heights of Initialized Rects to each other -> Sort
        for i in range(len(self.rects)):
            j = i
            while j > 0:
                if self.rects[j].height < self.rects[j - 1].height:
                    self.rects[j].x, self.rects[j - 1].x = self.rects[j - 1].x, self.rects[j].x # Swap X Positions before swapping Indexes
                    self.rects[j], self.rects[j - 1] = self.rects[j - 1], self.rects[j] # Swap Indexes
                    j -= 1 
                else:
                    self.draw() # Redraw rectangles at new positions
                    clock.tick(60)  # Controls animation speed
                    time.sleep(0.005)  # Slight delay for visibility
                    break


rectangle_10 = rectangles(240)
count = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black") 

    while count != 1:    
        rectangle_10.draw()
        count += 1
        pygame.display.flip()
        clock.tick(60)
        print("Sorting...")
        time.sleep(1.5)

    rectangle_10.sort_rects()

    pygame.display.flip()
    clock.tick(60)
    time.sleep(3)
    pygame.quit()

pygame.quit()