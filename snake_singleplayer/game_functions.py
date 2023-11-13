""" File that contains all functions for the snake game """
from random import randint
import pygame


def spawn_head_coordinates() -> tuple[int, int]:
    """ Function to generate the snake's head on the map """
    first_value = randint(0, 10)
    second_value = randint(0, 17)

    return first_value, second_value


def spawn_fruit_coordinates(snake_coordinates: list) -> tuple[int, int]:
    """ Function to generate a fruit on the map """
    while True:
        first_value = randint(0, 19)
        second_value = randint(0, 19)

        if not [first_value, second_value] in snake_coordinates:
            return first_value, second_value


def update_map(map_list: list, game_surface: pygame.rect):
    """ Function to update the drawed map """
    for y, line in enumerate(map_list):
        for x, value in enumerate(line):
            match value:
                case 0:  # empty
                    rect_to_draw = pygame.Rect(1 + 20 * x, 1 + 20 * y, 18, 18)
                    pygame.draw.rect(game_surface, "White", rect_to_draw)
                    pygame.draw.rect(game_surface, "Black", rect_to_draw, 2)
                case 1:  # snake head
                    rect_to_draw = pygame.Rect(1 + 20 * x, 1 + 20 * y, 18, 18)
                    pygame.draw.rect(game_surface, "chartreuse4", rect_to_draw)
                    pygame.draw.rect(game_surface, "Black", rect_to_draw, 2)
                case 2:  # snake back
                    rect_to_draw = pygame.Rect(1 + 20 * x, 1 + 20 * y, 18, 18)
                    pygame.draw.rect(game_surface, "chartreuse", rect_to_draw)
                    pygame.draw.rect(game_surface, "Black", rect_to_draw, 2)
                case 3:  # fruit
                    rect_to_draw = pygame.Rect(1 + 20 * x, 1 + 20 * y, 18, 18)
                    pygame.draw.rect(game_surface, "Red", rect_to_draw)
                    pygame.draw.rect(game_surface, "Black", rect_to_draw, 2)


def generate_game_borders(game_surface: pygame.Surface):
    """ Function to generate the border map """
    pygame.draw.rect(game_surface, "White", (0, 0, 400, 400), 2)
