import pygame
from settings import screen, font  
# Import screen and font settings from a settings module
from sprites import draw_game_elements, handle_event, update_charge, move_ball, move_goalie, draw_score_and_charge  
# Import game mechanics and drawing functions

# Game loop setup
running = True  
# Boolean to control the main game loop
clock = pygame.time.Clock()  
# Clock to manage the frame rate

while running:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            # Check for window close event
            running = False  
            # Exit the game loop
        else:
            handle_event(event)  
            # Handle other events like user input

    # Update game state
    update_charge()  
    # Update the kick charge if applicable
    move_ball()  
    # Update the ball's position and interactions
    move_goalie()  
    # Update the goalie's movement

    # Draw all game elements on the screen
    draw_game_elements(screen)  
    # Draw the field, ball, goal, and goalie
    draw_score_and_charge(screen)  
    # Draw the score and charge level

    # Refresh the display and control the frame rate
    pygame.display.flip()  
    # Update the display with the latest frame
    clock.tick(60)  
    # Cap the frame rate to 60 frames per second

# Quit Pygame once the loop ends
pygame.quit()
