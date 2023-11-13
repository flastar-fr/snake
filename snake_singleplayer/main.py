import pygame

from game import Game, display_score_and_stuffs
from ui_classes import GameStatsUI


width, height = 800, 500
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
pygame.display.set_icon(pygame.image.load("images\\snake.png"))

coords_game_vector = pygame.Vector2(100, 50)
main_game = Game(game_screen, 120, 0.5, coords_game_vector)
game_stats_screen = GameStatsUI(game_screen, pygame.Vector2(650, 100))
main_game.launch_game()

while True:
    main_game.handle_events()
    main_game.update()
    display_score_and_stuffs(main_game, game_stats_screen)
