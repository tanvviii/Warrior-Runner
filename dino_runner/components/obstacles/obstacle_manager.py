import pygame
import random

from dino_runner.components.obstacles.skeleton import Skeleton
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.goblin import Goblin

from dino_runner.utils.constants import *

INVINCIBLE_DURATION = 5

class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        
        if len(self.obstacles) == 0:
            random_obstacle = random.randint(0,2)

            if random_obstacle == 0:
                self.obstacles.append(Skeleton())
            elif random_obstacle == 1:
                self.obstacles.append(Bird(BIRD))
            elif random_obstacle == 2:
                self.obstacles.append(Goblin())

                # self.obstacles.append(Hole(HOLE))
                    
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)

            if game.player.mask.overlap(obstacle.mask,
                (obstacle.rect.x - game.player.dino_rect.x, 
                 obstacle.rect.y - game.player.dino_rect.y)):
                if not game.player.has_power_ups and game.lifes_left > game.last_life:
                    game.player.take_a_hit()
                    HIT_SOUND.set_volume(0.3)
                    HIT_SOUND.play()
                    self.obstacles.remove(obstacle)
                    game.lifes_left -= 1
                
                elif game.player.type == SHIELD_TYPE:
                    self.obstacles.remove(obstacle)
                    game.player.reset_dino_state()
                
                elif game.player.type == SWORD_TYPE and isinstance(obstacle, Bird):
                    self.obstacles.remove(obstacle)
                    SLASH_BIRD.set_volume(0.3)
                    SLASH_BIRD.play()
                elif game.player.type == SWORD_TYPE and isinstance(obstacle, Goblin):
                    self.obstacles.remove(obstacle)
                    SLASH_GOBLIN.set_volume(0.3)
                    SLASH_GOBLIN.play()
                elif game.player.type == SWORD_TYPE and isinstance(obstacle, Skeleton):
                    self.obstacles.remove(obstacle)
                    SLASH_SKELETON.set_volume(0.4)
                    SLASH_SKELETON.play()
                    game.player.reset_dino_state()

                else:
                    GAME_OVER.set_volume(0.4)
                    GAME_OVER.play()
                    pygame.time.delay(500)
                    game.playing = False
                    break


    def reset_obstacles(self):
        self.obstacles = []

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen) 