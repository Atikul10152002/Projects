import pygame
import random
pygame.init()
pygame.mixer.init()


sounds = []

ALL_SOUNDS = []

# for i in range(1, 4):
# 	sound = pygame.mixer.Sound(('music/file{}.ogg').format(i))
# 	sounds.append(sound)
list(map(lambda x: sounds.append(pygame.mixer.Sound(
    ('music/File{}.ogg').format(x))), range(1, 4)))


def playMusic():
    if pygame.mixer.music.get_busy() == True:
        print("oh no")
    for i in range(len(sounds)):
        sounds[i].stop()
        if sounds[i] not in ALL_SOUNDS:
            ALL_SOUNDS.append(sounds[i])

    random_index = random.choice(range(len(sounds)))
    sounds[random_index].play(-1)


playMusic()

shoot = pygame.mixer.Sound("music/Laser_Shoot_low.ogg")
shootM_gun = pygame.mixer.Sound("music/Laser_Shoot_high.ogg")
gainedPowerup = pygame.mixer.Sound("music/Beep6.ogg")
shut_down = pygame.mixer.Sound("music/Shut_Down1.ogg")
power_up = pygame.mixer.Sound("music/Power_Up1.ogg")
live_loss = pygame.mixer.Sound("music/Space_Alert1.ogg")
menu_item_sound = pygame.mixer.Sound("music/Beep1.ogg")


ALL_SOUNDS.extend((shoot, shootM_gun, gainedPowerup,
                   shut_down, power_up, live_loss, menu_item_sound))


def set_all_sounds(vol):
    for sound in ALL_SOUNDS:
        sound.set_volume(vol)
