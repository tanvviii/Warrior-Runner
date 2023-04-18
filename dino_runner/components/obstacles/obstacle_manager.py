import pygame
import random

from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0, 1)    

            if random_obstacle == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS + LARGE_CACTUS))
            elif random_obstacle == 1:
                self.obstacles.append(Bird(BIRD))
                    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.mask.overlap(obstacle.mask,
                (obstacle.rect.x - game.player.dino_rect.x, 
                 obstacle.rect.y - game.player.dino_rect.y)):
                pygame.time.delay(500)
                game.playing = False
                game.death_count += 1
                break  

    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 