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
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Upload ship image and get its rectangle.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Each new ship appears at the midbottom.
        self.rect.midbottom = self.screen_rect.midbottom

        # Float ship coordinate.
        self.x = float(self.rect.x)

        # Moving flags.
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """
        Update ship position based on flags.
        """
        # Update float X coordinate.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update actual X coordinate based on the float one.
        self.rect.x = self.x

    def blitme(self):
        """
        Draw ship at its current position.
        """
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """
        Center ship position.
        """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
