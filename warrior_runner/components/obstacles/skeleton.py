import random

from warrior_runner.components.obstacles.obstacle import Obstacle
from warrior_runner.utils.constants import SKELETON_IDLE


class Skeleton(Obstacle):
    def __init__(self):
        self.type = 0
        super().__init__(SKELETON_IDLE, self.type)
        self.rect.y = 100

    def update(self, game_speed, obstacles):
        self.type = 0 if self.type >= 7 else self.type

        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image[self.type // 2], self.rect)
        self.type += 1