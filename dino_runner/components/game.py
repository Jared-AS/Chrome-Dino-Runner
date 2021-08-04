import pygame
import random

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.large_cactus import LargeCactus
from dino_runner.components.small_cactus import SmallCactus
from dino_runner.components.bird import Bird
from dino_runner.components.player_lives import PlayerLives
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
        self.player_lives = PlayerLives()

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
        if self.player.invincible:
            time_to_show = round((self.player.invincible_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                fond = pygame.font.Font('freesansbold.ttf', 10)
                text = fond.render(f'Invincibility enabled for {time_to_show}',
                                   True,
                                   (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (800, 40)
                self.screen.blit(text, textRect)
            else:
                self.player.invincible = False

    def background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
        self.screen.fill((255, 255, 255))

        userInput = pygame.key.get_pressed()
        self.player.draw(self.screen)
        self.player.update(userInput)

    def run(self):
        # Game loop: events - update - draw
        self.create_components()
        self.playing = True
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.obstacles = []
        self.powerups = []
        self.when_star_appears = random.randint(200, 300) + self.points

    def update(self):
        if len(self.obstacles) == 0:
            if random.randint(0, 2) == 0:
                self.obstacles.append(SmallCactus(SMALL_CACTUS))
            elif random.randint(0, 2) == 1:
                self.obstacles.append(LargeCactus(LARGE_CACTUS))
            elif random.randint(0, 2) == 2:
                self.obstacles.append(Bird(BIRD))

        if len(self.powerups) == 0:
            if self.when_star_appears == self.points:
                self.when_star_appears = random.randint(self.when_star_appears + 200,
                                                        500 + self.when_star_appears)
                self.powerups.append(Star())

        for pwup in self.powerups:
            pwup.draw(self.screen)
            pwup.update(self.game_speed, self.powerups)
            if self.player.dino_rect.colliderect(pwup.rect):
                if pwup.type == 'star':
                    self.player.invincible = True
                    pwup.start_time = pygame.time.get_ticks()
                    self.player.invincible_time_up = pwup.start_time + 5000

        for obstacle in self.obstacles:
            obstacle.draw(self.screen)
            obstacle.update(self.game_speed, self.obstacles)
            if not self.player.invincible:
                if self.player.dino_rect.colliderect(obstacle.rect):
                    self.player_lives.reduce_live()
                    if self.player_lives.lives > 0:
                        self.player.invincible = True
                        start_time = pygame.time.get_ticks()
                        self.player.invincible_time_up = start_time + 1000
                    else:
                        pygame.time.delay(2000)
                        self.playing = False
                        break

        self.background()
        self.cloud.draw(self.screen)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.player_lives.draw(self.screen)
        pygame.display.update()

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

