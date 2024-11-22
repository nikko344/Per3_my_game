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

def draw_game_elements(screen):
    screen.fill(GREEN)
    pygame.draw.rect(screen, WHITE, (goal_x, goal_y, GOAL_WIDTH, GOAL_HEIGHT))  # Draw goal
    pygame.draw.rect(screen, BLACK, (goalie_x, goalie_y, GOALIE_WIDTH, GOALIE_HEIGHT))  # Draw goalie
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)  # Draw ball

def handle_event(event):
    global ball_in_motion, charging, charge, ball_speed_x, ball_speed_y
    if event.type == pygame.MOUSEBUTTONDOWN and not ball_in_motion:
        charging = True
        charge = 0
    elif event.type == pygame.MOUSEBUTTONUP and charging:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - ball_y, mouse_x - ball_x)
        ball_speed_x = charge * math.cos(angle)
        ball_speed_y = charge * math.sin(angle)
        ball_in_motion, charging = True, False

def update_charge():
    global charge
    if charging:
        charge = min(charge + 1, CHARGE_MAX)

def move_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, ball_in_motion, score
    if ball_in_motion:
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Ball collision with walls
        if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= SCREEN_WIDTH:
            ball_speed_x *= -1
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
            ball_speed_y *= -1

        # Ball collision with goalie
        if goalie_x < ball_x < goalie_x + GOALIE_WIDTH and goalie_y < ball_y < goalie_y + GOALIE_HEIGHT:
            ball_speed_x *= -1
            ball_speed_y *= -1

        # Check if the ball is in the goal
        if goal_x < ball_x < goal_x + GOAL_WIDTH and ball_y - BALL_RADIUS <= goal_y + GOAL_HEIGHT:
            score += 1
            reset_ball()

def move_goalie():
    global goalie_x, goalie_direction
    goalie_x += goalie_speed * goalie_direction
    if goalie_x <= goal_x or goalie_x + GOALIE_WIDTH >= goal_x + GOAL_WIDTH:
        goalie_direction *= -1

def draw_score_and_charge(screen):
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.draw.rect(screen, WHITE, (10, 50, charge * 10, 20))

def reset_ball():
    global ball_x, ball_y, ball_speed_x, ball_speed_y, ball_in_motion
    ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80
    ball_speed_x, ball_speed_y, ball_in_motion = 0, 0, False
