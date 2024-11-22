import pygame

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GOAL_WIDTH = 200
GOAL_HEIGHT = 20
GOALIE_WIDTH = 40
GOALIE_HEIGHT = 60
BALL_RADIUS = 20
CHARGE_MAX = 15  # Max charge for the kick

# Screen and font setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Soccer Game with Kick Charge and Goalie")
font = pygame.font.Font(None, 36)