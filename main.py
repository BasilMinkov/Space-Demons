import pygame

from system.game import Game

game = Game()

from loops.level import Level
from static_variables import DISPLAY_WIDTH, DISPLAY_HIGHT


def text_object(text, font):
    """ Returns PyGame text object and it's size """
    TextSurface = font.render(text, True, (250, 0, 0))
    return TextSurface, TextSurface.get_rect()


def message_display(text):
    """ Makes a text message in the center of a screen """
    largeText = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 90)
    TextSurf, TextRect = text_object(text, largeText)
    TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HIGHT / 2))
    game.params.gameDisplay.blit(TextSurf, TextRect)


def demons_dodged(count, distance):
    font = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 25)
    text = font.render('Scores: {}, Distance: {} km'.format(str(count), str(distance)), True, (250, 0, 0))
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

    game.run()
