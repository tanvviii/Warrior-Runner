import random

from dino_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = random.randint(240,320)
        self.is_moving = random.randint(0,3)
        self.up_n_down = False
    
    def update(self,game_speed, obstacles):
        if self.is_moving == 0:
            if not self.up_n_down:
                self.rect.y +=7
                if self.rect.y > 320:
                    self.up_n_down = True
            else:
                self.rect.y -=7
                if self.rect.y < 240:
                    self.up_n_down = False

        self.type = 0 if self.type >= 10 else self.type

        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image[self.type // 5], self.rect)
        self.type += 1