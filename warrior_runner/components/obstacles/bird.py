import random

from warrior_runner.components.obstacles.obstacle import Obstacle


class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 200
        if random.random() <= 0.7:
            self.rect.y = 160
        self.is_moving = random.random()
        self.up_n_down = False
    
    def update(self,game_speed, obstacles):
        if self.is_moving <= 0.25:
            if not self.up_n_down:
                self.rect.y +=7
                if self.rect.y > 200:
                    self.up_n_down = True
            else:
                self.rect.y -=7
                if self.rect.y < 140:
                    self.up_n_down = False

        self.type = 0 if self.type >= 15 else self.type

        super().update(game_speed, obstacles)

    def draw(self, screen):
        screen.blit(self.image[self.type // 2], self.rect)
        self.type += 1