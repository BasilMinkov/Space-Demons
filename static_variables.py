import os


def info():
    print("Static path: ", STATIC_PATH)
    print("Display Width: ", 1440, "Display Hight: ", 900)


STATIC_PATH = os.path.realpath(os.path.dirname(os.path.realpath(__file__)) + '/static')
DISPLAY_WIDTH, DISPLAY_HIGHT = 1440, 900
