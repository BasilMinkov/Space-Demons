import os
import sys
import pygame

from loops import Loop
from loops.menu import Menu
from static_variables import STATIC_PATH, DISPLAY_WIDTH, DISPLAY_HIGHT, WHITE, PURPLE


class Settings(Loop):

    def __init__(self, game):

        super().__init__(game)

        # global DISPLAY_WIDTH, DISPLAY_HIGHT

        dh = DISPLAY_WIDTH
        dw = DISPLAY_HIGHT
        control = "Keyboard"

        font = pygame.font.Font(os.path.join(STATIC_PATH, '9921.otf'), 50)
        comment = pygame.font.Font(os.path.join(STATIC_PATH, '9921.otf'), 20)

        settings = True

        backgroundImgHight = game.static.backgroundImg.get_rect().size[1]

        parallax = 0

        param_id = 0

        while settings:

            game.params.clock.tick(60)  # frames per second

            game.params.gameDisplay.blit(game.static.backgroundImg, (0, (0 - backgroundImgHight) + parallax))
            game.params.gameDisplay.blit(game.static.backgroundImg, (0, 0 + parallax))

            colours = [WHITE, WHITE, WHITE, WHITE]
            colours[param_id] = PURPLE

            text = font.render("Display Width: {}".format(dw), True, colours[0])
            game.params.gameDisplay.blit(text, (DISPLAY_WIDTH / 3, DISPLAY_HIGHT / 5))

            text = font.render("Display Hight: {}".format(dh), True, colours[1])
            game.params.gameDisplay.blit(text, (DISPLAY_WIDTH / 3, DISPLAY_HIGHT / 4))

            text = font.render("Accept", True, colours[2])
            game.params.gameDisplay.blit(text, (DISPLAY_WIDTH / 3, DISPLAY_HIGHT / 3))

            text = font.render("Control: {}".format(control), True, colours[3])
            game.params.gameDisplay.blit(text, (DISPLAY_WIDTH / 3, DISPLAY_HIGHT / 2))

            text = comment.render("Accept: Apply Changes    Backspace: Main Menu", True, WHITE)
            game.params.gameDisplay.blit(text, (DISPLAY_WIDTH / 3, DISPLAY_HIGHT / 1.1))

            parallax += 1

            if parallax >= backgroundImgHight:
                parallax = 0

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    pygame.mixer.Sound.play(game.static.change)
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()

                    if event.key == pygame.K_UP:
                        if param_id > 0:
                            param_id -= 1

                    if event.key == pygame.K_DOWN:
                        if param_id < 3:
                            param_id += 1

                    if event.key == pygame.K_RIGHT:
                        if param_id == 0:
                            dw += 100
                        if param_id == 1:
                            dh += 100
                        if param_id == 3:
                            if control == "Keyboard":
                                control = "BCI"
                                game.params.control = "BCI"
                            elif control == "BCI":
                                control = "Keyboard"
                                game.params.control = "Keyboard"

                    if event.key == pygame.K_LEFT:
                        # os.execv(__file__, sys.argv)

                        if param_id == 0:
                            dw -= 100
                        if param_id == 1:
                            dh -= 100
                        if param_id == 3:
                            if control == "Keyboard":
                                control = "BCI"
                                game.params.control = "BCI"
                            elif control == "BCI":
                                control = "Keyboard"
                                game.params.control = "Keyboard"

                    if event.key == pygame.K_RETURN and param_id == 2:
                        # переменные dw и dh записываются в settings.py
                        # TODO
                        os.execv(sys.executable, ['python'] + sys.argv)

                    if event.key == pygame.K_BACKSPACE:
                        Menu(game)

                if event.type == pygame.VIDEORESIZE:
                    print(event.w, event.h, event.size)

            pygame.display.update()
