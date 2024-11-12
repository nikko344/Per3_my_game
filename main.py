import pygame
from settings import screen, font
from sprites import draw_game_elements, handle_event, update_charge, move_ball, move_goalie, draw_score_and_charge

# Game loop
running = True
clock = pygame.time.Clock()