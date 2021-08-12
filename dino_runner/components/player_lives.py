import pygame
from dino_runner.utils.constants import (
    SCREEN_WIDTH,
    HEART,
    HEART_COUNT
)


class PlayerLives:
    def __init__(self):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH
        self.lives = HEART_COUNT

    def draw(self, screen):
        x = 10
        y = 20
        for counter in range(self.lives):
            screen.blit(HEART, (x, y))
            x += 30

    def reduce_live(self):
        self.lives -= 1

    def reset_lives(self):
        self.lives = HEART_COUNT