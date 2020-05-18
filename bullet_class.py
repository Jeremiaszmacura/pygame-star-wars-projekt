import math
import pygame

class Bullet:
    """Klasa definiująca pocisk wystrzeliwywany przez gracz."""

    """Klasa zawiera konstruktor oraz funkcje draw_bullet.
    Atrybutami funkcji są bullet_img, speed_y, position_x, position_y."""

    def __init__(self, player_position_x, player_position_y, player_size, speed = 4):
        self.bullet_img = pygame.image.load("assets/bullet_01.png")
        self.speed_y = speed
        self.position_x = player_position_x + player_size["x"] // 4
        self.position_y = player_position_y

    def draw_bullet(self, game_board):
        """Metoda rysuje obiekt pocisku na ekranie."""
        self.position_y -= self.speed_y
        game_board.screen.blit(self.bullet_img, (self.position_x, self.position_y))
        if(self.position_y <= 0):
            return True
        return False
