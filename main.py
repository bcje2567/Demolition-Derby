# Example file showing a basic pygame "game loop"
import pygame
 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=0
rot=0
class Car(pygame.sprite.Sprite):

    def __init__(self, health, speed, damage, width, height, angle):
        self.health=health
        self.speed=speed
        self.damage=damage
        self.height=height
        self.width=width
        self.angle=angle
        self.image = pygame.image.load("./Insporation/camoTruckNOBG.png")
        self.image_clean = self.image.copy()
        self.centerX = screen.get_width() // 2
        self.centerY = screen.get_height() // 2

    def re_draw(self):
        self.image = pygame.transform.rotate(self.image_clean, self.angle)
        self.rect = self.image.get_rect()
        self.rect.x = self.centerX
        self.rect.y = self.centerY
        screen.blit(self.image, self.rect)


truck_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
truck = Car(100, 20, 0, 100, 100, 0)
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")
    #pygame.draw.rect(screen, "blue",(100,100,100,100))
    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and truck.centerY >= 0:
        truck.centerY -= 300 * dt
        print("up")
    if keys[pygame.K_s] and truck.centerY <= 550:
        truck.centerY += 300 * dt
        print("down")
    if keys[pygame.K_a]: #and truck.centerX >= 0:
        rot += 10
        truck.angle = rot
        
    if keys[pygame.K_d]: #and truck.centerX <= 1180:
        rot -= 10
        truck.angle = rot

    # flip() the display to put your work on screen
    truck.re_draw()
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()