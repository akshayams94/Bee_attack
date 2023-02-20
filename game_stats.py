class GameStats():
	"""Track statistics for Alien Invasion."""
	
	def __init__(self, bee_settings):
		"""Initialize statistics."""
		self.bee_settings = bee_settings
		self.reset_stats()
		# Start Alien Invasion in an active state.
		self.game_active = False
		
	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.bee_settings.ship_limit
		self.score = 0
