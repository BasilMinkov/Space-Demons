from system.loader import Loader
from system.parameters import Parameters
from loops.menu import Menu


class Game:
    def __init__(self):
        # Load game system parameters
        self.params = Parameters()

        # Load static objects (images, sounds)
        self.static = Loader()

    @staticmethod
    def run():
        Menu()
