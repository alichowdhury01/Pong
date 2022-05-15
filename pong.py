from ctypes.wintypes import HACCEL
from ipaddress import collapse_addresses
from numpy import blackman
import pygame, sys

class Ball:
    def __init__(self, screen, color, posX, posY, radius):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy= 0
        self.show()

    def show(self):
        pygame.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def start_moving(self):
        self.dx = 15
        self.dy = 5

    def move(self):
        self.posX += self.dx
        self.posY += self.dy

class Paddle:
    def __init__(self, screen, color, posX, posY, width , height):
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.width = width
        self.height = height
        self.state = 'stopped'
        self.show()

    def show(self):
        pygame.draw.rect(self.screen, self.color, (self.posX, self.posY, self.width, self.height))

    def move(self):
        if self.state == 'up':
            self.posY -= 10

        elif self.state == 'down':
            self.posY += 10
pygame.init()

WIDTH = 900
HEIGHT = 500

# COLOR
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BLACK)
pygame.display.set_caption("PONG")

def paint_back():
    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)

paint_back()

ball = Ball(screen, WHITE, WIDTH//2, HEIGHT//2, 10)
paddle1 = Paddle(screen, WHITE, 15, HEIGHT//2 - 60, 20, 120)
paddle2 = Paddle(screen, WHITE, WIDTH - 20 - 15, HEIGHT//2 - 60, 20, 120)

# Variable
playing = False
FPS = 20
clock = pygame.time.Clock()

# Main loop
while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        # keyboard letter p to start the game 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                ball.start_moving()
                playing = True

            # Player1 up key = w
            if event.key == pygame.K_w:
                paddle1.state = 'up'
            
            # Player1 down key = s
            if event.key == pygame.K_s:
                paddle1.state = 'down'

            # Player2 up key = arrow up
            if event.key == pygame.K_UP:
                paddle2.state = 'up'
            
            # Player2 down key = arrow down 
            if event.key == pygame.K_DOWN:
                paddle2.state = 'down'

        if event.type == pygame.KEYUP:
            paddle1.state = 'stopped'
            paddle2.state = 'stopped'

    if playing:
        paint_back()

        # ball movement
        ball.move()
        ball.show()

        # Paddle1
        paddle1.move()
        paddle1.show()

        # Paddle2
        paddle2.move()
        paddle2.show()



    pygame.display.update()