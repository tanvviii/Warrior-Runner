from warrior_runner.utils.constants import HEART, DEFAULT_TYPE
from warrior_runner.components.power_ups.power_up import PowerUp


class ExtraLife(PowerUp):
    def __init__(self):
        super().__init__(HEART, DEFAULT_TYPE)