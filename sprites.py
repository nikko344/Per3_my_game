import pygame
import math
from settings import * 
# Import game settings such as screen size, colors, and object dimensions

# Initialize ball variables
ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80 
# Ball starts near the bottom center of the screen
ball_speed_x, ball_speed_y = 0, 0 
# Initial ball velocity is zero
ball_in_motion = False 
# Tracks whether the ball is currently moving

# Initialize goal position
goal_x, goal_y = SCREEN_WIDTH // 2 - GOAL_WIDTH // 2, 30  # Goal is centered at the top of the screen

# Initialize goalie position and movement variables
goalie_x = goal_x + GOAL_WIDTH // 2 - GOALIE_WIDTH // 2  
# Goalie starts in the middle of the goal
goalie_y = goal_y + GOAL_HEIGHT  
# Goalie is positioned slightly below the goal's top boundary
goalie_speed, goalie_direction = 4, 1  
# Speed of the goalie and its direction (1 = moving right, -1 = moving left)

# Initialize game variables
score = 0  
# Player's score starts at 0
charge, charging = 0, False  
# Tracks charge level and whether the ball is being charged for a kick

def draw_game_elements(screen):
    """Draw all game elements: field, goal, goalie, and ball."""
    screen.fill(GREEN)  
    # Fill the background with green color to represent a soccer field
    pygame.draw.rect(screen, WHITE, (goal_x, goal_y, GOAL_WIDTH, GOAL_HEIGHT))  
    # Draw the goal
    pygame.draw.rect(screen, BLACK, (goalie_x, goalie_y, GOALIE_WIDTH, GOALIE_HEIGHT))  
    # Draw the goalie
    pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)  
    # Draw the ball

def handle_event(event):
    """Handle user input events."""
    global ball_in_motion, charging, charge, ball_speed_x, ball_speed_y
    if event.type == pygame.MOUSEBUTTONDOWN and not ball_in_motion:
        charging = True  
        # Start charging the kick when mouse button is pressed
        charge = 0  
        # Reset the charge level
    elif event.type == pygame.MOUSEBUTTONUP and charging:
        # Calculate the angle of the kick based on mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()
        angle = math.atan2(mouse_y - ball_y, mouse_x - ball_x)
        ball_speed_x = charge * math.cos(angle)  
        # Set ball's horizontal speed
        ball_speed_y = charge * math.sin(angle)  
        # Set ball's vertical speed
        ball_in_motion, charging = True, False  
        # Start ball motion and stop charging

def update_charge():
    """Update the charge level while the kick is being charged."""
    global charge
    if charging:
        charge = min(charge + 1, CHARGE_MAX)  
        # Increment charge but cap it at a maximum value

def move_ball():
    """Move the ball and handle its interactions with walls, the goalie, and the goal."""
    global ball_x, ball_y, ball_speed_x, ball_speed_y, ball_in_motion, score
    if ball_in_motion:
        # Update ball position based on its velocity
        ball_x += ball_speed_x
        ball_y += ball_speed_y

        # Check for collision with screen edges
        if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= SCREEN_WIDTH:
            ball_speed_x *= -1  
            # Reverse horizontal direction on collision
        if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= SCREEN_HEIGHT:
            ball_speed_y *= -1  
            # Reverse vertical direction on collision

        # Check for collision with the goalie
        if goalie_x < ball_x < goalie_x + GOALIE_WIDTH and goalie_y < ball_y < goalie_y + GOALIE_HEIGHT:
            ball_speed_x *= -1  
            # Reverse horizontal direction
            ball_speed_y *= -1  
            # Reverse vertical direction

        # Check if the ball is in the goal
        if goal_x < ball_x < goal_x + GOAL_WIDTH and ball_y - BALL_RADIUS <= goal_y + GOAL_HEIGHT:
            score += 1  # Increment score
            reset_ball()  # Reset the ball's position and state

def move_goalie():
    """Move the goalie back and forth within the goal."""
    global goalie_x, goalie_direction
    goalie_x += goalie_speed * goalie_direction  
    # Update goalie position based on direction
    if goalie_x <= goal_x or goalie_x + GOALIE_WIDTH >= goal_x + GOAL_WIDTH:
        goalie_direction *= -1  
        # Reverse direction when goalie hits the goal's edges

def draw_score_and_charge(screen):
    """Draw the player's score and charge level on the screen."""
    score_text = font.render(f"Score: {score}", True, BLACK)  
    # Render the score text
    screen.blit(score_text, (10, 10))  
    # Display the score in the top-left corner
    pygame.draw.rect(screen, WHITE, (10, 50, charge * 10, 20))  
    # Draw the charge bar

def reset_ball():
    """Reset the ball's position and stop its motion."""
    global ball_x, ball_y, ball_speed_x, ball_speed_y, ball_in_motion
    ball_x, ball_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT - 80  
    # Reset to starting position
    ball_speed_x, ball_speed_y, ball_in_motion = 0, 0, False  
    # Stop the ball