import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


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

        # Fullscreen.
        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption('Alien Invasion')

        # Background color.
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """
        Launch main game cycle.
        """
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # Delete bullets which are not on the screen anymore.
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))

            self._update_screen()

    def _check_events(self):
        """
        Handle keyboard and mouse events.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """
        Handle keydown events.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """
        Handle keyup events.
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """
        Create new bullet and add it to the bullets group.
        """
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        """
        Update screen.
        """
        # On each cycle iteration screen is redrawn.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Display of the last drawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()
