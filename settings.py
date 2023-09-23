class Settings:
    """
    Class to store all settings of the 'Alien Invasion' game.
    """

    def __init__(self):
        """
        Initialize game settings.
        """
        # Screen parameters.
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)

        # Ship parameters.
        self.ship_speed = 0.5
