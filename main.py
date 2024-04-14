# Example file showing a basic pygame "game loop"
import pygame
 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

class Car(pygame.sprite.Sprite):

    def __init__(self, health, speed, damage, width, height):
        self.health=health
        self.speed=speed
        self.damage=damage
        self.height=height
        self.width=width

        self.image = pygame.image.load("./Insporation/camoTruckNOBG.png")

        centerX = screen.get_width() // 2
        centerY = screen.get_height() // 2

        self.rect = pygame.Rect(centerX, centerY, width, height)

        screen.blit(self.image, self.rect)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    pygame.draw.rect(screen, "blue",(100,100,100,100))
    # RENDER YOUR GAME HERE
    truck = Car(100, 20, 0, 100, 100)
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()