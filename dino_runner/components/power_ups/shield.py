from dino_runner.utils.constants import (
    SHIELD
)
from dino_runner.components.power_ups.powerup import PowerUp


class Shield(PowerUp):
    def __init__(self):
        self.image = SHIELD
        super(Shield, self).__init__(self.image)
