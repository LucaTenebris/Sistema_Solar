import pygame
from generic import Celestial_object

class Sun(Celestial_object):
    def __init__(self, image_path, mass,nucleo_status):
        super().__init__(image_path, mass)
        self.nucleo_status = nucleo_status
