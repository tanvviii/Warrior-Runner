import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.large_cactus import Large_Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 2)

            if random_obstacle == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(Large_Cactus(LARGE_CACTUS))
            elif random_obstacle == 2:
                self.obstacles.append(Bird(BIRD))
                    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.mask.overlap(obstacle.mask, 
                (obstacle.rect[0] - game.player.dino_rect.x, 
                 obstacle.rect[1] - game.player.dino_rect.y)):
                pygame.time.delay(500)
                game.playing = False
                break  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 