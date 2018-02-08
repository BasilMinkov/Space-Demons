import random
import pygame

from loops import Loop
from static_variables import DISPLAY_HIGHT, DISPLAY_WIDTH


class Level(Loop):

    def __init__(self, game):

        super().__init__(game)

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

            self.ring(coin_startX, coin_startY, coin_size, coin)
            coin_startY += coin_speed + boost
            distance += 1 + boost
            self.demons_dodged(score, distance)

            if counter > 5:
                self.spacecraft(game.static.spacecraftImg, x, y)
            else:
                self.spacecraft(game.static.spacecraft2Img, x, y)

            if x > DISPLAY_WIDTH - game.static.spacecraft_size[0] or x < 0:
                pygame.mixer.Sound.stop(game.static.soundtrack)
                pygame.mixer.Sound.play(game.static.returns)
                self.crash(game.static.explosion_1, game.static.explosion_2, game.static.backgroundImg, parallax, x, y)

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

    def spacecraft(self, img, x, y):
        self.game.params.gameDisplay.blit(img, (x, y))

    def ring(self, coinX, coinY, coin_size, img):
        img = pygame.transform.scale(img, (coin_size, coin_size))
        self.game.params.gameDisplay.blit(img, (coinX, coinY))

    def demons_dodged(self, count, distance):
        font = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 25)
        text = font.render('Scores: {}, Distance: {} km'.format(str(count), str(distance)), True, (250, 0, 0))
        self.game.params.gameDisplay.blit(text, (5, 0))

    def crash(self, img1, img2, bg, c, x, y):
        for i in range(1):
            self.message_display('GAME OVER!')
            self.game.params.gameDisplay.blit(img1, (x, y))
            pygame.display.update()

        pygame.time.wait(1000)
        # gameDisplay.blit(bg, (0, 0 + c))
        # gameDisplay.blit(img2, (x, y))
        # message_display('GAME OVER!')
        # pygame.display.update()
        # pygame.time.wait(1200)
        # gameDisplay.blit(bg, (0, 0 + c))
        Level()
