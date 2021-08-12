import random
import pygame

from dino_runner.components.obstacles.large_cactus import LargeCactus
from dino_runner.components.obstacles.small_cactus import SmallCactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import (
    SMALL_CACTUS,
    LARGE_CACTUS,
    BIRD
)


class ObstacleManager:

    def __init__(self):
        self.obstacles = []

    def reset_obstacles(self):
        self.obstacles = []

    def generate_obstacles(self):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))
        return self.obstacles

    def update(self, game):
        self.generate_obstacles()
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if not game.player.shield:
                    game.player_lives.reduce_live()
                    if game.player_lives.lives > 0:
                        game.player.shield = True
                        game.player.show_text = False
                        start_time = pygame.time.get_ticks()
                        game.player.shield_time_up = start_time + 1000
                    else:
                        pygame.time.delay(2000)
                        game.playing = False
                        break
                else:
                    self.obstacles.remove(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)