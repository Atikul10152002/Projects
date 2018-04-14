#!/usr/bin/env python3
import time
import pygame
import pickle
# from highscores import *
from music import *

pygame.init()
# import colors


infoObject = pygame.display.Info()
# screenWidth, screenHeight = 1600, 900
# screenWidth, screenHeight = 400, 300
screenWidth, screenHeight = infoObject.current_w, \
    infoObject.current_h

game_display_name = "RETROVE"
# screen = pygame.display.set_mode([screenWidth,
#                                   screenHeight], pygame.FULLSCREEN)
screen = pygame.display.set_mode([screenWidth, screenHeight])
print("Screen Resolution:", screenWidth, screenHeight)
pygame.display.set_caption(game_display_name)

#  highscore = {45800: 'asdf', 79200: 'Deanna!', 102600: 'Brandon', 22100: 'dadmanofwhitepowers',
#  23100: 'somaiya', 18900: '', 20900: '', 27900: '', 74400: 'austin', 26600: ''}

highscoreFilename = '.Highscore/highscores.pickle'
backup_highscoreFilename = '.Highscore/bak_highscores.pickle'

try:
    highscore = pickle.load(open(highscoreFilename, "rb"))
except Exception as e:
    print(e)
    highscore = pickle.load(open(backup_highscoreFilename, "rb"))
    pickle.dump(highscore, open(highscoreFilename, "wb"),
                protocol=pickle.HIGHEST_PROTOCOL)


highscoreOrgList = highscore
highscoreLinesNum = len(highscoreOrgList.keys())
sortedHighkeyList = sorted(highscoreOrgList.keys(), reverse=True)
sorted_highValue_list = [highscoreOrgList[key]
                         for key in sortedHighkeyList]

highscore = max(sortedHighkeyList)
highscore_name = sorted_highValue_list[sortedHighkeyList.index(
    highscore)]

"""
COLORS                                                          #COLORS
"""
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (178, 34, 34)
DARK_RED = (139, 58, 58)
REALLYRED = (220, 20, 60)
BLUE = (25, 25, 112)
DARK_BLUE = (16, 78, 139)
M_BLUE = (0, 191, 255)
DEEP_ORANGE = (255, 69, 0)
AMBER = (255, 97, 3)
INDIGO = (75, 0, 130)
PURPLE = (128, 0, 128)

Intro_title_color = AMBER
Intro_title_credit_color = RED
Highscore_btn_color = INDIGO
Start_btn_color = (0, 201, 87)
Quit_btn_color = DEEP_ORANGE
High_socre_background = (34, 79, 188)
BK_color = M_BLUE
# BK_color_shade = (0, 238, 238)
Back_btn_color = (100, 149, 237)
highscore_text_color = (255, 255, 255)
Btn_highlight_color = (255, 185, 15)

block_color_list = [BLACK, AMBER, DEEP_ORANGE, INDIGO]
block_color = (220, 20, 60)

start, FirstStart = time.time(), time.time()
elasped = 0
speed = constant_speed = 2.5
# increasingSpeed = 0.02
increasingSpeed = 0.005
globalxVel = globalyVel = 7
bullet_speed = screenHeight / 35
player_up_from_bottom = 150
starting_lives = 3
sartMachineGun, machineGunNum = False, False

done = False
powerupDuration = 120
Score_takeaway_for_powerup = 100
POWERUP_SCORE = 1000
player_width, player_height = 35, 46
# highscore = 0
playerx = screenWidth / 2
playery = screenHeight - player_height - \
    player_up_from_bottom
block_width, block_height = 35, 25
index, r_index = 0, 0


allSpritesList = pygame.sprite.Group()  # GROUP OF ALL SPRTIES
block_list = pygame.sprite.Group()  # GROUP OF ALL BLOCK
powerupList = pygame.sprite.Group()  # GROUP OF HEALTH POWERUP
powerupList2 = pygame.sprite.Group()  # GROUP OF MACHINE GUN POWERUP
bulletList = pygame.sprite.Group()  # GROUP OF BULLETS
player_list = pygame.sprite.Group()  # GROUP OF PLAYER *TECHNICALLY ONE PLAYER

# pygame.transform.scale2x(pygame.image.load(filepath).convert_alpha())

# FILEPATH FOR THE IMAGES
# Blocks -- >
powerup_image_des = pygame.transform.scale2x(pygame.image.load(
    "images/health_powerup.png").convert_alpha())
powerup2_image_des = pygame.transform.scale2x(
    pygame.image.load("images/bullet_powerup.png").convert_alpha())

# Assets -- >
player_image_des = pygame.transform.scale2x(
    pygame.image.load("images/player_png.png").convert_alpha())
bullet_image_des = pygame.transform.scale2x(
    pygame.image.load("images/bullet3.png").convert_alpha())
test_sub = pygame.transform.scale2x(pygame.image.load(
    "images/broken_health_powerup.png").convert_alpha())

# Sprites -- >
player_sprite_image_des = pygame.image.load(
    "Extra_img/fatbot.png").convert_alpha()
llama_image_des = pygame.image.load("images/llama.png").convert_alpha()

# backgorunds image to blit -- >
background_image_list = ["images/bac/memphis-colorful.png",
                         "images/bac/naturalblack.png",
                         "images/bac/dark-triangles.png",
                         "images/bac/gaming-pattern.png",
                         "images/bac/new_year_background.png"
                         ]
background_image = [pygame.image.load(filepath)
                    for filepath in background_image_list]

later_name = ''

num_block = int(screenWidth / 20)
numPowerup = numPowerup2 = 4
# bulletoffset = 7
IntroTitleOffset = 200
done = False
clock = pygame.time.Clock()
score, xVel, yVel = 0, 0, 0
# name = ""
random_name_gen = "ALPHALT"

# if __name__ == '__main__':
#     gameloop()
