"""

"""
# ====== imports block ================================== #
import pygame
import sys, os

from settings import Settings


# ====== class declaration ============================== #
class Ship():
    """Класс для управления кораблём."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задаёт его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        ship_img_path = os.path.dirname(sys.argv[0]) + '/' + 'images/ship.bmp'

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load(ship_img_path)
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


# ====== main code ====================================== #


# ====== end of code ==================================== #
