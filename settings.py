import pygame

# Initialize Pygame
pygame.init()

# Constants for game setup
SCREEN_WIDTH = 800  
# Width of the game window in pixels
SCREEN_HEIGHT = 600  
# Height of the game window in pixels

# Color definitions
WHITE = (255, 255, 255)  
# RGB color for white
BLACK = (0, 0, 0)        
# RGB color for black
GREEN = (0, 255, 0)      
# RGB color for green

# Goal dimensions
GOAL_WIDTH = 200  
# Width of the goal in pixels
GOAL_HEIGHT = 20  
# Height of the goal in pixels

# Goalie dimensions
GOALIE_WIDTH = 40  
# Width of the goalie in pixels
GOALIE_HEIGHT = 60  
# Height of the goalie in pixels

# Ball properties
BALL_RADIUS = 20  
# Radius of the ball in pixels

# Kick charge settings
CHARGE_MAX = 15  
# Maximum charge level for the ball's kick

# Screen and font setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  
# Create the game window
pygame.display.set_caption("Soccer Game with Kick Charge and Goalie")  
# Set the window title
font = pygame.font.Font(None, 36)  
# Initialize the font with a default size of 36