import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    Class to manage bullets.
    """

    def __init__(self, ai_game):
        """
        Create bullet object.
        """
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet at (0, 0) coordinates and set correct ones.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store coordinate in float variable.
        self.y = float(self.rect.y)

    def update(self):
        """
        Move bullet on top.
        """
        # Update float value.
        self.y -= self.settings.bullet_speed
        # Update actual coordinate.
        self.rect.y = self.y

    def draw_bullet(self):
        """
        Display bullet.
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
