import pygame

from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.cloud import Cloud
from dino_runner.components.player_lives import PlayerLives
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.power_ups.power_up_manager import PowerUpManager
from dino_runner.utils.constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    RUNNING,
    BG
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
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.player_lives = PlayerLives()

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        fond = pygame.font.Font('freesansbold.ttf', 20)

        text = fond.render('Points: ' + str(self.points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        self.screen.blit(text, text_rect)

        # showing star duration
        self.player.check_invincibility(self.screen)

    def draw_background(self):
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

    def run(self):
        # Game loop: events - update - draw
        self.create_components()
        self.playing = True
        self.player_lives.reset_lives()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def create_components(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.power_up_manager.update(self.points, self.game_speed, self.player)
        self.obstacle_manager.update(self)
        self.cloud.update(self.game_speed)

    def draw(self):
        self.score()
        self.clock.tick(FPS)
        self.draw_background()
        self.player_lives.draw(self.screen)
        self.player.draw(self.screen)
        self.cloud.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
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

