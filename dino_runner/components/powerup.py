import pygame
import random

from dino_runner.utils.constants import (
    SCREEN_HEIGHT
)

from pygame.sprite import Sprite


class PowerUp(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_HEIGHT + random.randint(800, 1000)
        self.rect.y = random.randint(100, 150)
        self.start_time = 0
        self.width = self.image.get_width()

    def update(self, game_speed, powerups):
        self.rect.x -= game_speed

        if self.rect.x < -self.rect.width:
            powerups.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, self.rect)

    @staticmethod
    def check_player_powerups(game, star):
        if len(game.powerups) == 0:
            if game.player.when_star_appears == game.points:
                game.player.when_star_appears = random.randint(game.player.when_star_appears + 200,
                                                        500 + game.player.when_star_appears)
                game.powerups.append(star)

        for pwup in game.powerups:
            pwup.draw(game.screen)
            pwup.update(game.game_speed, game.powerups)
            if game.player.dino_rect.colliderect(pwup.rect):
                if pwup.type == 'star':
                    game.player.invincible = True
                    pwup.start_time = pygame.time.get_ticks()
                    time_random = random.randrange(5, 8)
                    game.player.invincible_time_up = pwup.start_time + (time_random * 1000)
                    game.powerups.remove(pwup)

