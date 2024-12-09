import pygame
from generic import Celestial_object

class Asteroid(Celestial_object):
    def __init__(self, image_path, mass, distance, orbit_speed):
        super().__init__(image_path, mass, distance, orbit_speed)
        
