import pygame
from asteroid import Asteroid
from planet import Planet
from sun import Sun


SCREEN_WIDTH = 500
SCREEN_HEIGTH = 700
FPS = 60


screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGTH))
pygame.display.set_caption("Sistema Solar")

sol = Sun(image_path= "sol.png",mass= 2000, nucleo_status= "Active")

mercurio = Planet(image_path= "mercurio.png",
                   mass= 50,
                     distance= 100,
                     orbit_speed= 1.5,
                       nucleo_status= "Inactive")

marte = Planet(image_path= "marte.png",
                mass= 250,
                  distance= 180,
                  orbit_speed= 2,
                  nucleo_status= "Active")
asteroide = Asteroid(image_path= "asteroide.png",
                      mass = 20,
                      distance= 230,
                      orbit_speed= 1.999)

background_image = pygame.image.load("fondo.png").convert()
background_rect = background_image.get_rect()
clock = pygame.time.Clock()

runing = True

while runing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing = False
    
    screen.blit(background_image,background_rect)
    sol.draw(screen)
    mercurio.draw(screen)
    marte.draw(screen)
    asteroide.draw(screen)
    sol.update()
    mercurio.update()
    asteroide.update()
    marte.update()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
