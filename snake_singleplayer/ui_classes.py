import pygame


class DeathNWinUI:
    def __init__(self, surface: pygame.Surface):
        self.surface = surface
        self.coords_vector = [pygame.Vector2(200, 200), pygame.Vector2(200, 250)]
        self.fonts = (pygame.font.SysFont("Calibri", 50),
                      pygame.font.SysFont("Calibri", 30))

    def show_win_screen(self, score):
        for index, text in enumerate(["Win", f"Game Score {score}"]):
            generate_text(self.surface, self.fonts[index], text, self.coords_vector[index])

    def show_lose_screen(self, score):
        for index, text in enumerate(["Game Over", f"Game Score {score}"]):
            generate_text(self.surface, self.fonts[index], text, self.coords_vector[index])


class GameStatsUI:
    def __init__(self, surface: pygame.Surface, coords_vector: pygame.Vector2):
        self.surface = surface
        self.coords_vector = (coords_vector,
                              pygame.Vector2(coords_vector.x, coords_vector.y+50),
                              pygame.Vector2(coords_vector.x, coords_vector.y+80))
        self.fonts = (pygame.font.SysFont("Calibri", 40),
                      pygame.font.SysFont("Calibri", 35),
                      pygame.font.SysFont("Calibri", 35))

    def show_game_stats(self, score, fruits_nb, change_facing):
        to_show = [f"Score : {score}", f"Fruits : {fruits_nb}", f"Tourner : {change_facing}"]
        for index, text in enumerate(to_show):
            generate_text(self.surface, self.fonts[index], text, self.coords_vector[index])


def generate_text(surface: pygame.Surface, font: pygame.font, text: str, coords_vector: pygame.Vector2):
    """ Function to add a text to a surface easily """
    text = font.render(text, True, "White")
    text_rect = text.get_rect(center=(coords_vector.x, coords_vector.y))
    surface.blit(text, text_rect)
