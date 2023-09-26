import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien


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

        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        # Background color.
        self.bg_color = (230, 230, 230)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        # Create Play button.
        self.play_button = Button(self, 'Play')

    def run_game(self):
        """
        Launch main game cycle.
        """
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self, event):
        """
        Handle keydown events.
        """
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """
        Handle keyup events.
        """
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False

    def _check_play_button(self, mouse_pos):
        """
        Start new game if play button was pressed.
        """
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # Reset game statistics.
            self.stats.reset_stats()
            self.stats.game_active = True

            # Delete aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and center ship.
            self._create_fleet()
            self.ship.center_ship()

            # Hide mouse cursor.
            pygame.mouse.set_visible(False)

    def _fire_bullet(self):
        """
        Create new bullet and add it to the bullets group.
        """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """
        Update bullets' position and delete old bullets.
        """
        # Update bullets' position.
        self.bullets.update()

        # Delete bullets which are not on the screen anymore.
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

        if not self.aliens:
            # Delete all bullets and create a new fleet.
            self.bullets.empty()
            self._create_fleet()

    def _check_bullet_alien_collisions(self):
        """
        Handle alien and bullets collisions.
        """
        # Check if bullet has hit an alien.
        # If hit - delete an alien and a bullet.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _create_fleet(self):
        """
        Create alien fleet.
        """
        # Create alien.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - 2 * alien_width
        number_aliens_x = available_space_x // (2 * alien_width)

        # Define row count available.
        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - 3 * alien_height - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create first alien row.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """
        Create an alien and place him in the row.
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """
        Check if alien is near the corner.
        """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """
        Move the fleet down and change its direction.
        """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_aliens(self):
        """
        Update positions of all aliens.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Check collisions 'alien - ship'.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check if aliens have reached bottom of the screen.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """
        Handle hit between ship and alien.
        """
        if self.stats.ships_left > 0:
            # Decrease ships_left.
            self.stats.ships_left -= 1

            # Delete aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Create new fleet and put ship at the center.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_aliens_bottom(self):
        """
        Check if aliens have reached bottom.
        """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # Same as hitting ship and alien.
                self._ship_hit()
                break

    def _update_screen(self):
        """
        Update screen.
        """
        # On each cycle iteration screen is redrawn.
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        # Play button is displayed in case game is in inactive mode.
        if not self.stats.game_active:
            self.play_button.draw_button()

        # Display of the last drawn screen.
        pygame.display.flip()


if __name__ == '__main__':
    # Create an instance and launch the game.
    ai = AlienInvasion()
    ai.run_game()
