import time
import random
import pygame

from static_variables import DISPLAY_WIDTH, DISPLAY_HIGHT


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
        self.control = "Keyboard"
