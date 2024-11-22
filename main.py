import pygame
from settings import screen, font
from sprites import draw_game_elements, handle_event, update_charge, move_ball, move_goalie, draw_score_and_charge

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            handle_event(event)

    update_charge()
    move_ball()
    move_goalie()

    draw_game_elements(screen)
    draw_score_and_charge(screen)
    
    # Update display and set frame rate
    pygame.display.flip()
    clock.tick(60)

pygame.quit()