import pygame

from static_variables import DISPLAY_WIDTH, DISPLAY_HIGHT


class Loop:

    def __init__(self, game):

        self.game = game

        pass

    def text_object(self, text, font):
        """ Returns PyGame text object and it's size """
        TextSurface = font.render(text, True, (250, 0, 0))
        return TextSurface, TextSurface.get_rect()

    def message_display(self, text):
        """ Makes a text message in the center of a screen """
        largeText = pygame.font.Font('/Users/basilminkov/Library/Fonts/9921.otf', 90)
        TextSurf, TextRect = self.text_object(text, largeText)
        TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HIGHT / 2))
        self.game.params.gameDisplay.blit(TextSurf, TextRect)
