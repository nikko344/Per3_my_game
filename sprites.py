import pygame
import math
from settings import *

# Initialize ball, goal, goalie, and score variables
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80
ball_speed_x, ball_speed_y = 0, 0
ball_in_motion = False

goal_x, goal_y = SCREEN_WIDTH // 2 - GOAL_WIDTH // 2, 30

goalie_x = goal_x + GOAL_WIDTH // 2 - GOALIE_WIDTH // 2
goalie_y = goal_y + GOAL_HEIGHT
goalie_speed, goalie_direction = 4, 1  # 1 = right, -1 = left

score = 0
charge, charging = 0, False
