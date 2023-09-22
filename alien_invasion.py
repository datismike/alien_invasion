import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """
    Class to manage resources and game behavior.
    """

    def __init__(self):
        """
        Initialize game and create game resources.
        """
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Background color.
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)

    def run_game(self):
        """
        Launch main game cycle.
        """
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """
        Handle keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _update_screen(self):
        """
        Update screen.
        """
        # On each cycle iteration screen is redrawn.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        # Display of the last drawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()
