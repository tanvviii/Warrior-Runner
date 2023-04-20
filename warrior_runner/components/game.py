import pygame
import time

from warrior_runner.utils.constants import *
from warrior_runner.components.warrior import Warrior
from warrior_runner.components.obstacles.obstacle_manager import ObstacleManager
from warrior_runner.components.power_ups.power_manager import PowerUpManager


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(GAME_WALLPAPER)

        self.parallax_speeds = [1, 0.075, 0.15, 0.3, 0.6]

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 20

        self.score = 0
        self.best_score = 0

        self.lives_left = 3
        self.last_life = 0
        self.heart_vec = [HEARTS[0]] * 3

        self.x_pos_bg = [0, 0, 0, 0, 0]

        self.y_pos_bg = 380

        self.player = Warrior()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()

    def execute(self):
        LOOP_MENU.set_volume(0.3)
        LOOP_MENU.play(-1)
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()

        pygame.display.quit()
        pygame.quit()

    def run(self):
        LOOP_MENU.fadeout(300)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups()
        self.reset()
        while self.playing:
            self.events()
            self.update()
            self.draw()

    def reset(self):
        self.lives_left = 3
        self.game_speed = 20
        self.score = 0

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.update_heart()
        self.update_score()
        self.power_up_manager.update(self)

    def update_score(self):
        self.score += 1
        if self.score % 100 == 0:
            self.game_speed += 2
    
    def update_heart(self):
        for i in range(len(self.heart_vec)):
            self.heart_vec[i] = HEARTS[0]
            if self.lives_left - 1 < i:
                self.heart_vec[i] = HEARTS[1]

    def draw_text(self, phrase, size, position, rgb):
        font = pygame.font.Font(FONT_STYLE, size)
        text = font.render(phrase, True, rgb)
        text_rect = text.get_rect()
        text_rect.center = position
        self.screen.blit(text, text_rect)

    def draw_score(self):
        self.screen.blit(SCORE, (0, -65))
        self.draw_text(
            f"{self.score}", 31,
            (1010, 110), (255,255,255)
            )
        self.draw_text(
            f"{self.score}", 28,
            (1010, 110), (0,0,0)
            )
    
    def draw_hearts_left(self):
        for i in range(len(self.heart_vec)):
            self.screen.blit(self.heart_vec[i], (10 + i * 50,10))

    def draw_power_up_time(self):
        if self.player.has_power_ups:
            if self.player.extra_life:
                self.player.has_power_ups = False
                self.player.type = DEFAULT_TYPE
                self.player.extra_life = False
            else:
                time_to_show = round((self.player.power_up_time - pygame.time.get_ticks()) / 1000, 2)

                if time_to_show >= 0:
                    self.draw_text(
                        f"{self.player.type.capitalize()} for {time_to_show} seconds", 16,
                        (550, 50), (0,0,0)
                    )
                else:
                    self.player.has_power_ups = False
                    self.player.type = DEFAULT_TYPE

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((174, 222, 203))
        self.draw_background()
        self.draw_floor()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.draw_score()
        self.draw_hearts_left()
        self.draw_power_up_time()
        self.power_up_manager.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_floor(self):
        self.parallax(BG, 0, 12)

    def draw_background(self):
        self.parallax(PLX_1, 1, -50)
        self.parallax(PLX_2, 2, -50)
        self.parallax(PLX_3, 3, -50)
        self.parallax(PLX_4, 4, -50)

    def parallax(self, image, speed_index, y_pos=0):
        speed = self.parallax_speeds[speed_index]
        x_pos = self.x_pos_bg[speed_index]
        image_width = image.get_width()
        self.screen.blit(image, (x_pos, y_pos))
        self.screen.blit(image, (image_width + x_pos, y_pos))
        if x_pos <= -image_width:
            self.screen.blit(image, (image_width + x_pos, y_pos))
            x_pos = 0
        x_pos -= self.game_speed * speed
        self.x_pos_bg[speed_index] = x_pos

    def handle_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def show_menu(self):
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.score > self.best_score:
            self.best_score = self.score

        if self.lives_left == 3:
            self.screen.blit(START_SCREEN, (0,0))
            self.screen.blit(GAME_TITLE, (0,0))

            self.draw_text(
                "Press any key to start", 22,
                (half_screen_width, half_screen_height + 60), (0,0,0)
                )
        elif self.lives_left == self.last_life:
            pygame.mixer.music.fadeout(500)
            self.screen.blit(SKULL, (half_screen_width - 45, half_screen_height - 140))    
            self.draw_text(
                "Press any key to Restart", 22,
                (half_screen_width, half_screen_height), (0,0,0)
                )
            self.draw_text(
                f"Score: {self.score}", 22,
                (half_screen_width, half_screen_height + 40), (0,0,0)
                )
            self.draw_text(
                f"Best Score: {self.best_score}", 22,
                (half_screen_width, half_screen_height + 75), (0,0,0)
                )

        pygame.display.flip()

        self.handle_events_on_menu()