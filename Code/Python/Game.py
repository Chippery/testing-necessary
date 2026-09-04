import pygame
import math

# pygame setup
pygame.init()
width = 1280
height = 720
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
screen_rect = screen.get_rect()
center = screen_rect.center
running = True
gravity = 2
bounce = 0.8

class ball:
    def __init__(self, radius, color, xpos=center[0], ypos=center[1], thickness=0):
        self.xpos = xpos
        self.ypos = ypos
        self.radius = radius
        self.color = color
        self.thickness = thickness
        self.vx = 5
        self.vy = 0
        self.circle = None

    def draw(self):
        self.circle = pygame.draw.circle(
            screen, self.color, (int(self.xpos), int(self.ypos)), self.radius, self.thickness
        )

    def check_gravity(self):
        self.vy += gravity
        self.ypos += self.vy
        self.xpos += self.vx
        
        floor = height - self.radius
        ceiling = self.radius

        # Collision w/Floor & Ceiling 
        if self.ypos >= floor:
            self.ypos = floor
            self.vy *= -bounce

        elif self.ypos <= ceiling:
            self.ypos = ceiling
            self.vy *= -bounce

        # Collision w/Left & Right Walls
        if self.xpos + self.radius >= width:
            self.xpos = width - self.radius
            self.vx *= -bounce

        elif self.xpos - self.radius <= 0:
            self.xpos = self.radius
            self.vx *= -bounce

    def check_collision(self, other):
        """
        Handles collision of this (inner) ball against another ball acting as a containment circle.
        """

        # center of the outer ball
        cx = other.xpos
        cy = other.ypos

        # distance from inner ball to outer ball center
        dx = self.xpos - cx
        dy = self.ypos - cy
        dist = math.hypot(dx, dy)

        # max distance allowed from center
        max_dist = other.radius - self.radius

        # if the inner ball goes beyond the inner edge:
        if dist > max_dist:
            # normal vector
            nx = dx / dist
            ny = dy / dist

            # clamp position back to inside the outer circle
            self.xpos = cx + nx * max_dist
            self.ypos = cy + ny * max_dist

            # reflect velocity along boundary normal
            dot = self.vx * nx + self.vy * ny
            self.vx -= 2 * dot * nx
            self.vy -= 2 * dot * ny




ball1 = ball(30, 'red', center[0], 75)
ball2 = ball(300, 'red', center[0], center[1], 3)  # OUTER BALL

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    ball1.check_gravity()
    ball1.check_collision(ball2)

    ball2.draw()  # outer circle first
    ball1.draw()  # inner ball second

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
