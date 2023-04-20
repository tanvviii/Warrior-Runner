import pygame
from pygame.sprite import Sprite

from warrior_runner.utils.constants import *

X_POS = 80
Y_POS = 275
X_DUNK = 80
Y_DUNK = Y_POS
Y_SHADOW = 397
JUMP_VEL = 8.5

RUN_IMG = {
    DEFAULT_TYPE: RUNNING,
    SHIELD_TYPE: RUNNING_SHIELD,
    SWORD_TYPE: RUNNING_SWORD
    }
DUCK_IMG = {
    DEFAULT_TYPE: DUCKING, 
    SHIELD_TYPE: DUCKING_SHIELD,
    SWORD_TYPE: DUCKING
    }
JUMP_IMG = {
    DEFAULT_TYPE: JUMPING, 
    SHIELD_TYPE: JUMPING_SHIELD,
    SWORD_TYPE: JUMPING
    }
FALL_IMG = {
    DEFAULT_TYPE: FALLING, 
    SHIELD_TYPE: FALLING_SHIELD,
    SWORD_TYPE: FALLING
}
HIT_IMG = {
    DEFAULT_TYPE: HURT
}
DEAD_IMG = {
    DEFAULT_TYPE: DEAD
}


class Warrior(Sprite):
    def __init__(self):
        self.type = DEFAULT_TYPE
        self.image = RUN_IMG[self.type][0]
        self.shadow = SHADOW[0]
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

        self.warrior_rect.x = X_POS
        self.last_x_pos = X_POS
        self.warrior_rect.y = Y_POS

        self.step_index = 0
        self.jump_vel = JUMP_VEL
        self.warrior_jump = False
        self.half_jump = False

        self.warrior_run = True
        self.warrior_duck = False
        self.setup_state()

    def setup_state(self):
        self.has_power_ups = False
        # self.shield = False
        self.extra_life = 0
        self.show_text = False
        self.power_up_time = 0

    def reset_warrior_state(self):
        self.setup_state()
        self.type = DEFAULT_TYPE
    
    def update_player_position(self):
        self.warrior_rect.x = self.last_x_pos

    def update(self, user_input):
        self.update_player_position()

        if self.warrior_run:
            self.run()
        elif self.warrior_jump or self.half_jump:
            self.jump()
        elif self.warrior_duck:
            self.duck()

        if user_input[pygame.K_UP] and not (self.warrior_jump or self.half_jump):
            JUMP_SOUND.set_volume(0.3)
            JUMP_SOUND.play()
            self.warrior_jump = True
            self.warrior_run = False
            self.warrior_duck = False
            self.half_jump = True
        elif user_input[pygame.K_DOWN] and not (self.warrior_jump or self.half_jump):
            self.warrior_duck = True
            self.warrior_run = False
            self.warrior_jump = False

        if user_input[pygame.K_RIGHT]:
            self.last_x_pos += 10
            if self.last_x_pos > 400:
                self.last_x_pos = 400
        elif user_input[pygame.K_LEFT]:
            self.last_x_pos -= 10
            if self.last_x_pos < 1:
                self.last_x_pos = 1

        elif not self.warrior_duck and not (self.warrior_jump or self.half_jump):
            self.warrior_duck = False
            self.warrior_run = True
            self.warrior_jump = False

        if self.step_index >= 15:
            self.step_index = 0

    def run(self):
        self.update_shadow(self.step_index // 8)

        self.image = RUN_IMG[self.type][self.step_index // 2]
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.update_player_position()
        self.warrior_rect.y = Y_POS
        self.step_index += 1

    def jump(self):
        self.update_shadow(self.step_index // 8, (22 * 2.2, 6 * 2.2))

        if self.warrior_jump:
            self.image = JUMP_IMG[self.type][self.step_index // 8]
            self.mask = pygame.mask.from_surface(self.image)
            self.warrior_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            self.half_jump = False
        
        if self.warrior_rect.y == 77:
            self.half_jump = True
            self.warrior_jump = False
        
        if self.half_jump:
            self.image = FALL_IMG[self.type][self.step_index // 8]
            self.mask = pygame.mask.from_surface(self.image)
            self.warrior_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
    
        if self.jump_vel < -JUMP_VEL:
            self.warrior_rect.y = Y_POS
            self.jump_vel = JUMP_VEL
            self.warrior_run = True
            self.half_jump = False

    def duck(self):
        self.update_shadow(1, (23 * 6, 6 * 3), 156)

        self.image = DUCK_IMG[self.type][self.step_index // 5]
        self.warrior_rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.update_player_position()
        self.warrior_rect.y = Y_DUNK
        self.step_index += 1
        self.warrior_duck = False

    def take_a_hit(self):    
        self.image = HIT_IMG[self.type]

    def die(self):
        self.warrior_rect.y = Y_POS
        self.image = DEAD_IMG[self.type]

    def update_shadow(self, index, scale=(22 * 3, 6 * 3), opacity=128):
        self.shadow = SHADOW[index]
        self.shadow = pygame.transform.scale(self.shadow, scale)
        self.shadow.set_alpha(opacity)

    def draw(self, screen):
        self.update_player_position()
        if self.warrior_jump:
            screen.blit(self.shadow, (self.last_x_pos + 60, Y_SHADOW))
        elif self.warrior_duck:
            screen.blit(self.shadow, (self.last_x_pos + 8, Y_SHADOW))
        else:
            screen.blit(self.shadow, (self.last_x_pos + 40, Y_SHADOW))

        screen.blit(self.image, (self.last_x_pos, self.warrior_rect.y))