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
        self.settings = ai_game.settings

        # Load alien image and setup rect attribute.
        self.image = pygame.image.load('images/alien1.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears in the top left corner.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Float horizontal alien position.
        self.x = float(self.rect.x)

    def check_edges(self):
        """
        True if alien is near the corner.
        """
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        """
        Move alien right or left.
        """
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x
