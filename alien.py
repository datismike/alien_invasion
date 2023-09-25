import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    Class to manage single alien.
    """

    def __init__(self, ai_game):
        """
        Initialize alien and setup start position.
        """
        super().__init__()
        self.screen = ai_game.screen

        # Load alien image and setup rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Float horizontal alien position.
        self.x = float(self.rect.x)
