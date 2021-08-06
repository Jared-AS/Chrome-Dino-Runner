import pygame
import random

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.large_cactus import LargeCactus
from dino_runner.components.small_cactus import SmallCactus
from dino_runner.components.bird import Bird
from dino_runner.components.star import Star
from dino_runner.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    RUNNING,
    BG,
    SMALL_CACTUS,
    LARGE_CACTUS,
    BIRD
)
from dino_runner.components.powerup import PowerUp
from dino_runner.components.obstacle import Obstacle

TITLE = 'Chrome Dino Runner'
ICON = pygame.image.load('assets/DinoWallpaper.png')
FPS = 30


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = True
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.points = 0
        self.player = Dinosaur()
        self.cloud = Cloud()
        self.powerups = []
        self.obstacles = []

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        fond = pygame.font.Font('freesansbold.ttf', 20)

        text = fond.render('Points: ' + str(self.points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        self.screen.blit(text, textRect)

        # showing star duration
        self.player.check_invincibility(self.screen)

    def background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def run(self):
        # Game loop: events - update - draw
        self.obstacles = []
        self.powerups = []
        self.player.when_star_appears = random.randint(200, 300) + self.points
        self.playing = True
        while self.playing:
            self.events()
            self.update()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        self.screen.fill((255, 255, 255))

    def init_obstacles(self):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

    def update(self):
        userInput = pygame.key.get_pressed()
        self.player.draw(self.screen)
        self.player.update(userInput)

        PowerUp.check_player_powerups(self, Star())

        self.init_obstacles()
        Obstacle.check_player_obstacles(self)

        self.background()
        self.cloud.draw(self.screen)

        self.cloud.update(self.game_speed)

        self.score()

        self.clock.tick(FPS)
        pygame.display.update()
        pygame.display.flip()

    def show_menu(self, death_count=0):
        self.running = True
        self.screen.fill((255, 255, 255))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render('Press any Key to Start', True, (0, 0,
                                                                0))
        elif death_count > 0:
            text = font.render('Press any Key to Restart', True, (0, 0,
                                                                  0))
            score = font.render('Your Score: ' + str(self.points), True, (0,
                                                                     0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
                                + 50)
            self.screen.blit(score, scoreRect)
        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.screen.blit(text, textRect)
        self.screen.blit(RUNNING[0], (SCREEN_WIDTH // 2 - 20, SCREEN_HEIGHT
                                 // 2 - 140))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

