import pygame


class Ship:
    """
    Class to manage ship.
    """

    def __init__(self, ai_game):
        """
        Initialize ship and set its start position.
        """
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Upload ship image and get its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the midbottom.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """
        Draw ship at its current position.
        """
        self.screen.blit(self.image, self.rect)
