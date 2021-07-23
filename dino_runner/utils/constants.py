import pygame
import os

# Global Constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
IMG_DIR = os.path.join(os.path.dirname(__file__), '..', 'assets')

# Assets Constants
RUNNING = [pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun1.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoRun2.png'))]
JUMPING = pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoJump.png'))
DUCKING = [pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck1.png')),
           pygame.image.load(os.path.join(IMG_DIR, 'Dino/DinoDuck2.png'))]

SMALL_CACTUS = [pygame.image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus1.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus2.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'Cactus/SmallCactus3.png'))]
LARGE_CACTUS = [pygame.image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus1.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus2.png')),
                pygame.image.load(os.path.join(IMG_DIR, 'Cactus/LargeCactus3.png'))]

BIRD = [pygame.image.load(os.path.join(IMG_DIR, 'Bird/Bird1.png')),
        pygame.image.load(os.path.join(IMG_DIR, 'Bird/Bird2.png'))]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png'))

BG = pygame.image.load(os.path.join(IMG_DIR, 'Other/Track.png'))
