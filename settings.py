class Settings:
    """
    Class to store all settings of the 'Alien Invasion' game.
    """

    def __init__(self):
        """
        Initialize game settings.
        """
        # Screen parameters.
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)

        # Ship parameters.
        self.ship_speed = 0.5
        self.ship_limit = 3

        # Bullet parameters.
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Alien parameters.
        self.alien_speed = 2
        self.fleet_drop_speed = 10
        # 1 - moving right; 2 - moving left.
        self.fleet_direction = 1
