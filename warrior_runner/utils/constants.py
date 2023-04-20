import pygame
import os

pygame.mixer.init()
pygame.display.init()


# Global Constants
TITLE = "Warrior Runner"
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
FPS = 30
IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "assets")
FONT_STYLE = "warrior_runner/assets/Fonts/m42.ttf"
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Music Assets
LOOP_GAME = pygame.mixer.music.load("warrior_runner/assets/Musics/loop_game.mp3")
LOOP_MENU = pygame.mixer.Sound("warrior_runner/assets/Musics/loop_menu.mp3")
JUMP_SOUND = pygame.mixer.Sound("warrior_runner/assets/Musics/jumpSound.mp3")
HIT_SOUND = pygame.mixer.Sound("warrior_runner/assets/Musics/hitSound.mp3")
SLASH_GOBLIN = pygame.mixer.Sound("warrior_runner/assets/Musics/slashGoblin.wav")
SLASH_BIRD = pygame.mixer.Sound("warrior_runner/assets/Musics/slashBird.wav")
SLASH_SKELETON = pygame.mixer.Sound("warrior_runner/assets/Musics/slashSkeleton.wav")
GAME_OVER = pygame.mixer.Sound("warrior_runner/assets/Musics/gameOverHit.wav")
LIFE_UP = pygame.mixer.Sound("warrior_runner/assets/Musics/lifeUp.wav")

# Animation Constants
DEAD = pygame.image.load(os.path.join(IMG_DIR, "Character/char_dead/dead.png")).convert_alpha()

RUNNING = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_3.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_4.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_5.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_6.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_run/sprite_7.png")).convert_alpha()
]

SHADOW = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/Shadow/shadow_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/Shadow/shadow_1.png")).convert_alpha(),
]

RUNNING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_3.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_4.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_5.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_6.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_run/shieldRun_7.png")).convert_alpha()
]

RUNNING_SWORD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_3.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_4.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_7.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_8.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_9.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_attack/Warrior_Dash-Attack_10.png")).convert_alpha(),
]

JUMPING = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_jump/Warrior_Jump_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_jump/Warrior_Jump_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_jump/Warrior_Jump_3.png")).convert_alpha(),
    ]

FALLING = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_fall/Warrior_Fall_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_fall/Warrior_Fall_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_fall/Warrior_Fall_3.png")).convert_alpha(),
]

FALLING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_fall/shieldFall_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_fall/shieldFall_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_fall/shieldFall_2.png")).convert_alpha(),
]

HURT = pygame.image.load(os.path.join(IMG_DIR, "Character\char_hurt\Warrior-hit_0.png")).convert_alpha()


JUMPING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_jump/shieldJump_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_jump/shieldJump_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_jump/shieldJump_2.png")).convert_alpha(),
    ]

DUCKING = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_slide/Warrior-Slide_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_slide/Warrior-Slide_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_slide/Warrior-Slide_3.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_slide/Warrior-Slide_4.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/char_slide/Warrior-Slide_5.png")).convert_alpha()
    ]

DUCKING_SHIELD = [
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_slide/shieldSlide_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_slide/shieldSlide_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Character/shield_slide/shieldSlide_2.png")).convert_alpha(),
]

BIRD = [
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird3.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird4.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird5.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird6.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Bird/Bird7.png")).convert_alpha(),
]

GOBLIN_IDLE = [
    pygame.image.load(os.path.join(IMG_DIR, "Goblin/goblin_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Goblin/goblin_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Goblin/goblin_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Goblin/goblin_3.png")).convert_alpha(),
]

SKELETON_IDLE = [
    pygame.image.load(os.path.join(IMG_DIR, "Skeleton/skeleton_0.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Skeleton/skeleton_1.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Skeleton/skeleton_2.png")).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, "Skeleton/skeleton_3.png")).convert_alpha(),
]

CLOUD = pygame.image.load(os.path.join(IMG_DIR, 'Other/Cloud.png')).convert_alpha()
SHIELD = pygame.image.load(os.path.join(IMG_DIR, 'Other/shield.png')).convert_alpha()
SWORD = pygame.image.load(os.path.join(IMG_DIR, 'Other/hammer.png')).convert_alpha()

BG = pygame.image.load(os.path.join(IMG_DIR, 'Parallax_BG/floor.png')).convert_alpha()

PLX_1 = pygame.image.load(os.path.join(IMG_DIR, 'Parallax_BG/plx-1.png')).convert_alpha()
PLX_2 = pygame.image.load(os.path.join(IMG_DIR, 'Parallax_BG/plx-2.png')).convert_alpha()
PLX_3 = pygame.image.load(os.path.join(IMG_DIR, 'Parallax_BG/plx-3.png')).convert_alpha()
PLX_4 = pygame.image.load(os.path.join(IMG_DIR, 'Parallax_BG/plx-4.png')).convert_alpha()

HEART = pygame.image.load(os.path.join(IMG_DIR, 'Other/SmallHeart.png')).convert_alpha()

DEFAULT_TYPE = "default"
SHIELD_TYPE = "shield"
SWORD_TYPE = "sword"

# Interface Assets

SCORE = pygame.image.load(os.path.join(IMG_DIR, 'Interface/Score.png')).convert_alpha()
HEARTS = [
    pygame.image.load(os.path.join(IMG_DIR, 'Interface/HeartsFull.png')).convert_alpha(),
    pygame.image.load(os.path.join(IMG_DIR, 'Interface/HeartsEmpty.png')).convert_alpha()
]

START_SCREEN = pygame.image.load(os.path.join(IMG_DIR, 'Interface/StartScreen.png')).convert_alpha()
GAME_TITLE = pygame.image.load(os.path.join(IMG_DIR, 'Interface/GameTittle.png')).convert_alpha()
SKULL = pygame.image.load(os.path.join(IMG_DIR, "Interface/DeathScreen.png")).convert_alpha()
GAME_WALLPAPER = pygame.image.load(os.path.join(IMG_DIR, "GameWallpape.png")).convert_alpha()