import pygame
import math

class Celestial_object():
    def __init__(self, image_path,mass, distance = 0, orbit_speed = 0):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.__mass = mass
        self.distance = distance
        self.__orbit_speed = 0
        self.orbit_speed = orbit_speed
        self.mass = mass
    @property
    def orbit_speed(self):
        return self.__orbit_speed
    @orbit_speed.setter
    def orbit_speed(self,value):
        if 0 <= value <= 10:
            self.__orbit_speed = value
        else:
            raise ValueError('Error en la Velocidad de Orbita')
    
    @property
    def mass(self):
        return self.__mass
    @mass.setter
    def mass(self,value):
        if 10 <= value <= 2500:
            self.__mass = value
        else:
            raise ValueError('Rango equivocado de masa') 

    
    
    def update(self):
        self.angle += self.orbit_speed

    def draw(self,screen):
        x = (screen.get_width() // 2 ) + (self.distance * math.cos(math.radians(self.angle)))
        y = (screen.get_height() // 2) + (self.distance * math.sin(math.radians(self.angle)))
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image,self.rect)