from dino_runner.utils.constants import (
    HAMMER
)
from dino_runner.components.power_ups.powerup import PowerUp


class HammerPowerUp(PowerUp):
    def __init__(self):
        self.image = HAMMER
        self.type = "hammer"
        super(HammerPowerUp, self).__init__(self.image, self.type )
