import pygame
from generic import Celestial_object
class Planet(Celestial_object):
    def __init__(self, image_path, mass, distance, orbit_speed,nucleo_status):
        super().__init__(image_path, mass, distance, orbit_speed)
        self.nucleo_status = nucleo_status
        