import pygame

from static_variables import DISPLAY_HIGHT
from loops import Loop
from loops.level import Level
from system.loader import Loader


class Menu(Loop):

    def __init__(self, game):

        super().__init__(game)

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
                        Level(game)

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
