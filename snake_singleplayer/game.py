import pygame
from sys import exit
import time

from game_functions import spawn_head_coordinates, spawn_fruit_coordinates, update_map, generate_game_borders
from snake import Snake
from timer import Timer
from ui_classes import DeathNWinUI, GameStatsUI


class Game:
    def __init__(self, screen: pygame.display, tick_rate: int, speed: int | float, coords: pygame.Vector2):
        pygame.init()
        self.screen = screen
        self.tick_rate = tick_rate
        self.speed = speed
        self.clock = pygame.time.Clock()

        # game objects
        self.coords_vector = coords
        self.game_surface = pygame.Surface((400, 400))
        self.death_n_win_screen = DeathNWinUI(self.game_surface)
        generate_game_borders(self.game_surface)

        # game attributs
        self.game_map_list = None
        self.snake = None
        self.fruit_coordinates = None
        self.win = None
        self.lose = None
        self.previous_sec = None
        self.start_time = None
        self.timer = None
        self.last_direction_change_time = None

        self.screen.blit(self.game_surface, (self.coords_vector.x, self.coords_vector.y))

    def launch_game(self):
        """ Method to initialize a game """
        head_coordinates = spawn_head_coordinates()
        self.snake = Snake(head_coordinates[0], head_coordinates[1])
        self.fruit_coordinates = spawn_fruit_coordinates(self.snake.body)
        self.win = False
        self.lose = False
        self.previous_sec = 0
        self.start_time = time.time()
        self.last_direction_change_time = pygame.time.get_ticks()

    def handle_events(self):
        """ Method to verify all events """
        # close window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # game commands
            elif event.type == pygame.KEYDOWN and not self.lose:
                current_time = pygame.time.get_ticks()
                if current_time - self.last_direction_change_time >= 250:
                    if event.key == pygame.K_UP:
                        self.snake.change_facing("N")
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_facing("S")
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_facing("E")
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_facing("W")
                    self.last_direction_change_time = current_time

    def update(self):
        """ Method to run to update the game """
        if not self.lose and not self.win:  # if not player lose
            # re initialize to display
            self.game_surface.fill("black")
            generate_game_borders(self.game_surface)
            self.game_map_list = [[0 for _ in range(20)] for _ in range(20)]

            # display snake and fruit
            self.game_map_list[self.fruit_coordinates[0]][self.fruit_coordinates[1]] = 3
            self.game_map_list[self.snake.body[0][0]][self.snake.body[0][1]] = 1
            for part in self.snake.body[1:]:
                y_part = part[0]
                x_part = part[1]
                if 0 <= x_part <= 19 and 0 <= y_part <= 19:
                    self.game_map_list[y_part][x_part] = 2

            # move snake and fruit
            elapsed_time = time.time() - self.start_time
            if elapsed_time >= self.previous_sec:
                self.previous_sec += self.speed
                self.snake.move()
                if self.snake.check_fruit_condition(self.fruit_coordinates):  # snake ate foot
                    self.snake.extend()
                    self.fruit_coordinates = spawn_fruit_coordinates(self.snake.body)
                    self.snake.fruits += 1

                # verify lose and win
                if self.snake.check_lose_conditions():
                    self.lose = True
                    self.timer = Timer(1, 4)

                elif self.snake.check_win_condition():
                    self.win = True
                    self.timer = Timer(1, 4)

            # screen writing
            update_map(self.game_map_list, self.game_surface)

        elif self.lose:  # if player lose
            # re initialize to display
            self.game_surface.fill("black")
            generate_game_borders(self.game_surface)

            # lose screen
            self.death_n_win_screen.show_lose_screen(self.get_score())

            # lose timer
            if self.timer.compare_time():
                self.launch_game()

        elif self.win:  # if player win
            self.game_surface.fill("black")
            generate_game_borders(self.game_surface)

            # win screen
            self.death_n_win_screen.show_win_screen(self.get_score())

            # win timer
            if self.timer.compare_time():
                self.launch_game()

        # actualize game
        self.screen.blit(self.game_surface, (self.coords_vector.x, self.coords_vector.y))
        pygame.display.update()
        self.clock.tick(self.tick_rate)

    # getters
    def get_snake_facing_change(self):
        return self.snake.changing_facing

    def get_nb_fruits(self):
        return self.snake.fruits

    def get_score(self):
        return self.get_nb_fruits() * 3 - self.get_snake_facing_change() * 0.5


def display_score_and_stuffs(game: Game, game_stats_screen: GameStatsUI):
    """ Method to display the score and all informations about """
    game.screen.fill("black")
    game_stats_screen.show_game_stats(game.get_score(),
                                      game.get_nb_fruits(),
                                      game.get_snake_facing_change())
