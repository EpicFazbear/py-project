import pygame
import math
import sys

pygame.init()
scrsize = width, height = int(1000), int(750)
screen = pygame.display.set_mode(scrsize)
clock = pygame.time.Clock()
# Mapsize: 100x75, 10px per block
# Padding: 1-2px

SIZE = int(20)
TICK = int(60)


class Snake:
    def __init__(self):
        self.Color = (0, 255, 0) # The color of the snake
        self.Direction = "NONE" # Stays still until this is updated
        self.Speed = 2 # How many times the snake will move per second

        self.PosX = int(width/2) # Internal variable used to store the snake's X position
        self.PosY = int(height/2) # Internal variable used to store the snake's Y position
        self.Entity = pygame.Rect(self.PosX, self.PosY, int(SIZE), int(SIZE)) # Actual Rect entity of the snake
        self.Tick = 0 # Internal variable used to control the snake speed
        self.Speed = TICK / self.Speed # Used later in the tick loop
        screen.fill(self.Color, self.Entity)
        pygame.display.update(self.Entity)

    def ChangeDirection(self, direction):
        print("Changing to " + self.Direction)
        self.Direction = direction

    def CheckTick(self):
        self.Tick += 1
        if math.fmod(self.Tick, self.Speed) == 0:
            return True

    def NONE(self):
        if self.CheckTick():
            print("Going " + self.Direction)

    def UP(self):
        if self.CheckTick():
            print("Going " + self.Direction)
            self.PosY -= SIZE
            self.Entity = pygame.Rect(self.PosX, self.PosY, int(SIZE), int(SIZE))
            screen.fill(self.Color, self.Entity)
            pygame.display.update(self.Entity)

    def DOWN(self):
        if self.CheckTick():
            print("Going " + self.Direction)
            self.PosY += SIZE
            self.Entity = pygame.Rect(self.PosX, self.PosY, int(SIZE), int(SIZE))
            screen.fill(self.Color, self.Entity)
            pygame.display.update(self.Entity)

    def LEFT(self):
        if self.CheckTick():
            print("Going " + self.Direction)
            self.PosX -= SIZE
            self.Entity = pygame.Rect(self.PosX, self.PosY, int(SIZE), int(SIZE))
            screen.fill(self.Color, self.Entity)
            pygame.display.update(self.Entity)

    def RIGHT(self):
        if self.CheckTick():
            print("Going " + self.Direction)
            self.PosX += SIZE
            self.Entity = pygame.Rect(self.PosX, self.PosY, int(SIZE), int(SIZE))
            screen.fill(self.Color, self.Entity)
            pygame.display.update(self.Entity)


Gaben = Snake() # Gaben the Snake :D

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                Gaben.ChangeDirection("UP")
            elif event.key == pygame.K_s:
                Gaben.ChangeDirection("DOWN")
            elif event.key == pygame.K_a:
                Gaben.ChangeDirection("LEFT")
            elif event.key == pygame.K_d:
                Gaben.ChangeDirection("RIGHT")

    getattr(Gaben, Gaben.Direction)()
    clock.tick(TICK)
