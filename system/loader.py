import os
import pygame

from static_variables import STATIC_PATH


class Loader:
    def __init__(self):
        # loading sounds
        self.soundtrack = self.load_sound('soundtrack.wav')
        self.beep = self.load_sound('Beep17.wav')
        self.change = self.load_sound('change.wav')
        self.returns = self.load_sound('return.wav')

        # loading spacecraft image
        self.spacecraft_size = (150, 150)
        self.spacecraftImg = pygame.transform.scale(self.load_image('spacecraft.png'), self.spacecraft_size)
        self.spacecraft2Img = pygame.transform.scale(self.load_image('spacecraft_2.png'), self.spacecraft_size)

        # loading background image
        self.backgroundImg = self.load_image('background.png')

        # loading explosion image
        self.explosion_1 = pygame.transform.scale(self.load_image('explosion_1.tiff'), (150, 150))
        self.explosion_2 = pygame.transform.scale(self.load_image('explosion_2.tiff'), (150, 150))

        # loading demon images
        self.coin_1 = self.load_image('sonicring-1.png')
        self.coin_2 = self.load_image('sonicring-2.png')
        self.coin_3 = self.load_image('sonicring-3.png')
        self.coin_4 = self.load_image('sonicring-4.png')
        self.coins = [self.coin_1, self.coin_2, self.coin_3, self.coin_4]

        # loading title image
        self.title_1 = self.load_image('title_1.png')
        self.title_2 = self.load_image('title_2.png')
        self.new_game = self.load_image('new_game.png')
        self.load_game = self.load_image('load_game.png')
        self.settings = self.load_image('settings.png')
        self.credits = self.load_image('credits.png')

    @staticmethod
    def load_image(name):
        """ Load image and return image object"""
        fullname = os.path.join(STATIC_PATH, 'images', name)
        image = pygame.image.load(fullname)
        return image

    @staticmethod
    def load_sound(name):
        """ Load sound and return sound object"""
        fullname = os.path.join(STATIC_PATH, 'sounds', name)
        sound = pygame.mixer.Sound(fullname)
        return sound
