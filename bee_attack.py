import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button

def run_game():
	# Initialize game and create a screen object
	pygame.init()
	bee_settings = Settings()
	
	screen = pygame.display.set_mode((bee_settings.screen_width, bee_settings.screen_height))
	
	pygame.display.set_caption("Alien Invasion")
	
	# Make the Play button.
	play_button = Button(bee_settings, screen, "START")
	
	# Create an instance to store game statistics.
	stats = GameStats(bee_settings)
	
	# Make a ship
	ship = Ship(bee_settings, screen)
	
	# Make a group to store bullets in.
	bullets = Group()
	
	# Make a group of aliens.
	aliens = Group()
	
	# Create the fleet of aliens.
	gf.create_fleet(bee_settings, screen, ship, aliens)
	
	# Start the main loop for the game
	while True:
		# Watch for the keyboard and mouse events
		gf.check_events(bee_settings, screen, stats, play_button, ship, bullets)
		if stats.game_active:
			ship.update()
			gf.update_bullets(bee_settings, screen, ship, aliens, bullets)
			gf.update_aliens(bee_settings, stats, screen, ship, aliens, bullets)
		
		gf.update_screen(bee_settings, screen, stats, ship, aliens, bullets, play_button)
	
run_game()
