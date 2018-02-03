import sys
import os
import pygame
import numpy as np
import random
import time

STATIC_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/static')
DISPLAY_WIDTH, DISPLAY_HIGHT = 1440, 900
print("Static path: ", STATIC_PATH)
print("Display Width: ", 1440, "Display Hight: ", 900)

white = (255, 255, 255)


class Game:
    def __init__(self):
        # Load game system parameters
        self.params = Parameters()

        # Load static objects (images, sounds)
        self.static = Loader()

    @staticmethod
    def run():
        Menu()


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


class Parameters:

    def __init__(self):
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HIGHT), (pygame.FULLSCREEN | pygame.HWSURFACE))
        pygame.display.set_caption("Space Race")
        random.seed(time.time())
        self.clock = pygame.time.Clock()

        self.gameDisplay.fill((0, 0, 0))
        pygame.display.update()

        random.seed(time.time() * 1000)

        self.running = True


class Loop:

    def __init__(self):
        pass


class Menu(Loop):

    def __init__(self):

        super().__init__()

        intro = True
        title = True

        backgroundImgHight = game.static.backgroundImg.get_rect().size[1]
        print("Background image hight: ", backgroundImgHight)
        planet = Loader.load_image('p1.png')

        menu = [game.static.new_game,
                game.static.load_game,
                game.static.settings,
                game.static.credits]

        menu_id = 0

        planet_X = -150
        planet_Y = DISPLAY_HIGHT / 4
        planet_movementX = 0
        planet_movementY = 0

        planet_hight = 200
        planet_width = 200
        planet_hight_distortion = 0
        planet_width_distortion = 0

        parallax = 0

        planet = pygame.transform.scale(planet, (planet_hight + 300, planet_width + 300))

        while intro:

            game.params.clock.tick(60)

            if parallax == backgroundImgHight:
                parallax = 0

            game.params.gameDisplay.blit(game.static.backgroundImg, (0, (0 - backgroundImgHight) + parallax))
            game.params.gameDisplay.blit(game.static.backgroundImg, (0, 0 + parallax))

            game.params.gameDisplay.blit(planet, (planet_X + planet_movementX, planet_Y + planet_movementY))

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(game.static.change)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_DOWN:
                        if menu_id < 4:
                            menu_id += 1
                        if menu_id == 4:
                            menu_id = 0
                    if event.key == pygame.K_UP:
                        if menu_id == -1:
                            menu_id = 3
                        if menu_id > -1:
                            menu_id -= 1
                    if event.key == pygame.K_RETURN and menu_id == 0:
                        Level()

            if title:
                game.params.gameDisplay.blit(game.static.title_1, (0, 0))
                title = False
            else:
                game.params.gameDisplay.blit(game.static.title_2, (0, 0))
                title = True

            parallax += 1

            planet_movementX += 1
            planet_movementY = planet_movementX * 0.25

            planet_width_distortion += 1
            planet_hight_distortion += 1

            game.params.gameDisplay.blit(menu[menu_id], (0, 0))
            pygame.display.update()


class Level(Loop):

    def __init__(self):

        super().__init__()

        backgroundImgHight = game.static.backgroundImg.get_rect().size[1]

        x = DISPLAY_WIDTH * 0.45  # OX spacecraft start position
        y = DISPLAY_HIGHT * 0.8  # OY spacecraft start position

        x_change = 0

        coin = game.static.coins[0]
        coin_size = 65
        coin_startX = random.randrange(500, DISPLAY_WIDTH - 500)
        coin_startY = -200
        coin_speed = 5

        gameExit = False
        speed_up = False

        score = 0
        distance = 0
        counter = 0
        coin_state = 1
        parallax = 0
        sps = 0
        boost = 0
        delayB = 0
        delayM = 0
        delayP = 0

        pygame.mixer.Sound.play(game.static.soundtrack, loops=-1)

        while not gameExit:

            game.params.clock.tick(60)  # frames per second
            parallax += 3
            parallax += boost
            if parallax >= backgroundImgHight:
                parallax = 0

            for event in pygame.event.get():  # list of events per t

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_LEFT:
                        x_change = -20
                    if event.key == pygame.K_RIGHT:
                        x_change = 20

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0

            x += x_change

            game.params.gameDisplay.blit(game.static.backgroundImg, (0, 0 - backgroundImgHight + parallax))
            game.params.gameDisplay.blit(game.static.backgroundImg, (0, 0 + parallax))

            counter += 1

            if counter > 10:
                counter = 0

            ring(coin_startX, coin_startY, coin_size, coin)
            coin_startY += coin_speed + boost
            distance += 1 + boost
            demons_dodged(score, distance)

            if counter > 5:
                spacecraft(game.static.spacecraftImg, x, y)
            else:
                spacecraft(game.static.spacecraft2Img, x, y)

            if x > DISPLAY_WIDTH - game.static.spacecraft_size[0] or x < 0:
                pygame.mixer.Sound.stop(game.static.soundtrack)
                pygame.mixer.Sound.play(game.static.returns)
                crash(game.static.explosion_1, game.static.explosion_2, game.static.backgroundImg, parallax, x, y)

            if coin_startY > DISPLAY_HIGHT:
                coin_startY = -coin_size
                coin_startX = random.randrange(50, DISPLAY_WIDTH - 50)

            if coin_state < 10:
                coin = game.static.coins[0]
            elif 10 <= coin_state < 20:
                coin = game.static.coins[1]
            elif 20 <= coin_state < 30:
                coin = game.static.coins[2]
            elif 30 <= coin_state < 40:
                coin = game.static.coins[3]

            coin_state += 1
            if coin_state >= 40:
                coin_state = 1

            if y <= coin_startY + coin_size:

                if x > coin_startX \
                        and x < coin_startX + coin_size \
                        or x + game.static.spacecraft_size[0] > coin_startX \
                                and x + game.static.spacecraft_size[0] < coin_startX + coin_size \
                        or x < coin_startX \
                                and x + game.static.spacecraft_size[0] > coin_startX + coin_size:

                    pygame.mixer.Sound.play(game.static.beep)
                    coin_startY = -coin_size
                    coin_startX = random.randrange(500, DISPLAY_WIDTH - 500)
                    score += 1
                    speed_up = True

            if speed_up == True:
                sps += 5
                # delayB = 30
                speed_up = False

            if sps > 0 and delayP == 0:
                boost += 1
                sps -= 1
                delayP = 0
            elif sps > 0:
                delayP -= 1

            if sps == 0 and boost > 0 and delayM == 0:
                boost -= 1
                delayM = 10
            if sps == 0 and boost > 0:
                delayM -= 1

            if boost > 30:
                boost = 30

            pygame.display.update()  # .flip()


def text_object(text, font):
    """ Returns PyGame text object and it's size """
    TextSurface = font.render(text, True, white)
    return TextSurface, TextSurface.get_rect()


def message_display(text):
    """ Makes a text message in the center of a screen """
    largeText = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 90)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HIGHT / 2))
    game.params.gameDisplay.blit(TextSurf, TextRect)


def demons_dodged(count, distance):
    font = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 25)
    text = font.render('Scores: {}, Distance: {} km'.format(str(count), str(distance)), True, white)
    game.params.gameDisplay.blit(text, (5, 0))


# Characters


def spacecraft(img, x, y):
    game.params.gameDisplay.blit(img, (x, y))


def ring(coinX, coinY, coin_size, img):
    img = pygame.transform.scale(img, (coin_size, coin_size))
    game.params.gameDisplay.blit(img, (coinX, coinY))


# Passive Loops


def crash(img1, img2, bg, c, x, y):
    for i in range(1):
        message_display('GAME OVER!')
        game.params.gameDisplay.blit(img1, (x, y))
        pygame.display.update()

    pygame.time.wait(1000)
        # gameDisplay.blit(bg, (0, 0 + c))
        # gameDisplay.blit(img2, (x, y))
        # message_display('GAME OVER!')
        # pygame.display.update()
        # pygame.time.wait(1200)
        # gameDisplay.blit(bg, (0, 0 + c))
    Level()


if __name__ == "__main__":
    game = Game()
    game.run()
