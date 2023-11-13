import pygame as pg

from game_assets.game import Game, display_score_and_stuffs


width, height = 800, 500
game_screen = pg.display.set_mode((width, height))
pg.display.set_caption("Snake")
pg.display.set_icon(pg.image.load("images\\snake.png"))

main_game = Game(game_screen, 120, 0.5, 100, 50)
main_game.launch_game()

while True:
    main_game.handle_events()
    main_game.update()
    display_score_and_stuffs(main_game, 650, 100)
