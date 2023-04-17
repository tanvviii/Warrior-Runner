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

        # dino_hitbox = pygame.sprite.GroupSingle(game.player)
        # obstacle_hitbox = pygame.sprite.GroupSingle(self.obstacles)
                    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            # if pygame.sprite.spritecollide(dino_hitbox.sprite, obstacle_hitbox,False, pygame.sprite.collide_mask):
            #     pygame.time.delay(500)
            #     game.playing = False
            #     break 

            if game.player.mask.overlap(obstacle.mask, 
                (obstacle.rect.x - game.player.dino_rect.x, 
                obstacle.rect.y - game.player.dino_rect.y)):
                pygame.time.delay(500)
                game.playing = False
                break  

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 