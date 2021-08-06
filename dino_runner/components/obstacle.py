from dino_runner.utils.constants import (
    SCREEN_WIDTH,
)
from pygame.sprite import Sprite
from pygame.time import delay


class Obstacle(Sprite):

    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH

    def update(self, game_speed, obstacles):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

    @staticmethod
    def check_player_obstacles(game):
        for obstacle in game.obstacles:
            obstacle.draw(game.screen)
            obstacle.update(game.game_speed, game.obstacles)
            if not game.player.invincible:
                if game.player.dino_rect.colliderect(obstacle.rect):
                    delay(2000)
                    game.playing = False
                    break
