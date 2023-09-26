class GameStats():
    """
    Handle game statistics.
    """

    def __init__(self, ai_game):
        """
        Initialize statistics.
        """
        self.settings = ai_game.settings
        self.reset_stats()

        # Game starts in an active mode.
        self.game_active = True

    def reset_stats(self):
        """
        Initialize game statistics.
        """
        self.ships_left = self.settings.ship_limit
