import random
import pygame

from dino_runner.components.power_ups.star import Star


class PowerUpManager:

    def __init__(self):
        self.power_ups = []
        self.when_star_appears = 0
        self.points = 0

    def reset_power_ups(self, points):
        self.power_ups = []
        self.points = points
        self.when_star_appears = random.randint(200, 300) + self.points

    def generate_power_ups(self, points):
        self.points = points
        if len(self.power_ups) == 0:
            if self.when_star_appears == self.points:
                print("generating powerup")
                self.when_star_appears = random.randint(self.when_star_appears + 200, 500 + self.when_star_appears)
                self.power_ups.append(Star())
        return self.power_ups

    def update(self, points, game_speed, player):
        self.generate_power_ups(points)
        for power_up in self.power_ups:
            power_up.update(game_speed, self.power_ups)
            if player.dino_rect.colliderect(power_up.rect):
                if power_up.type == 'star':
                    player.invincible = True
                    power_up.start_time = pygame.time.get_ticks()
                    player.invincible_time_up = power_up.start_time + 5000

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)
