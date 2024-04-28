# Example file showing a basic pygame "game loop"
import pygame
 
# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=0
class Car(pygame.sprite.Sprite):

    def __init__(self, health, speed, damage, width, height, angle):
        self.health=health
        self.speed=speed
        self.damage=damage
        self.height=height
        self.width=width
        self.angle=angle
        self.image = pygame.image.load("./Insporation/camoTruckNOBG.png")

        self.centerX = screen.get_width() // 2
        self.centerY = screen.get_height() // 2

    def re_draw(self):
        
        print(self.angle)   
        # self.rect = pygame.Rect(self.centerX, self.centerY, self.width, self.height)

        screen.blit(self.image, self.image.get_rect())

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
    if keys[pygame.K_s] and truck.centerY <= 550:
        truck.centerY += 300 * dt
    if keys[pygame.K_a]: #and truck.centerX >= 0:
        truck.angle -= 1 * dt
        truck.image = pygame.transform.rotate(truck.image, 1) 
    # if keys[pygame.K_d]: #and truck.centerX <= 1180:
    #     truck.angle += 15

    # flip() the display to put your work on screen
    truck.re_draw()
    pygame.display.flip()

    dt = clock.tick(60) / 1000 # limits FPS to 60

pygame.quit()