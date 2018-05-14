import os
import sys
import pygame
import random
pygame.init()
pygame.mixer.init()

executing_wd = os.path.dirname(os.path.realpath(sys.argv[0]))
current_wd = os.path.join(executing_wd, "assets")
music_wd = os.path.join(current_wd, "music")

sounds = []
ALL_SOUNDS = []
# music_wd = variables.music_wd

list(map(lambda x: sounds.append(pygame.mixer.Sound(
    (os.path.join(music_wd, f'File{x}.ogg')))), range(1, 4)))


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

shoot = pygame.mixer.Sound(os.path.join(music_wd, "Laser_Shoot_low.ogg"))
shootM_gun = pygame.mixer.Sound(os.path.join(music_wd, "Laser_Shoot_high.ogg"))
gainedPowerup = pygame.mixer.Sound(os.path.join(music_wd, "Beep6.ogg"))
shut_down = pygame.mixer.Sound(os.path.join(music_wd, "Shut_Down1.ogg"))
power_up = pygame.mixer.Sound(os.path.join(music_wd, "Power_Up1.ogg"))
live_loss = pygame.mixer.Sound(os.path.join(music_wd, "Space_Alert1.ogg"))
menu_item_sound = pygame.mixer.Sound(os.path.join(music_wd, "Beep1.ogg"))


ALL_SOUNDS.extend((shoot, shootM_gun, gainedPowerup,
                   shut_down, power_up,
                   live_loss, menu_item_sound))


def set_all_sounds(vol):
    for sound in ALL_SOUNDS:
        sound.set_volume(vol)
