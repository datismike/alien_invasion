import sys
import pygame


class AlienInvasion:
    """
    Class to manage resources and game behavior.
    """

    def __init__(self):
        """
        Initialize game and create game resources.
        """
        pygame.init()

        self.screen = pygame.display.set_mode((600, 400))
        pygame.display.set_caption('Alien Invasion')

        # Background color.
        self.bg_color = (230, 230, 230)

    def run_game(self):
        """
        Launch main game cycle.
        """
        while True:
            # Handle keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # On each cycle iteration screen is redrawn.
            self.screen.fill(self.bg_color)

            # Display of the last drawn screen.
            pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()
