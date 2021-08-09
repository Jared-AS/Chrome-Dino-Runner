from dino_runner.utils.constants import (
    STAR
)
from dino_runner.components.PowerUps.powerup import PowerUp


class Star(PowerUp):
    def __init__(self):
        self.type = "star"
        self.image = STAR
        super(Star, self).__init__(self.image, self.type)
