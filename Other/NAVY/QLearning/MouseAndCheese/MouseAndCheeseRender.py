from threading import Thread

import pygame, sys
from pygame.locals import *
from numpy import ndarray
import numpy as np
import time

SLEEP_TIME = 0.5
BOARD_SIZE = 8
TALE_SIZE = 64
SCREEN_WIDTH = BOARD_SIZE * TALE_SIZE
SCREEN_HEIGHT = BOARD_SIZE * TALE_SIZE

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
LIGHTSKYBLUE = (135, 206, 250)

assets = {
    "mouse": pygame.image.load("../assets/mouse.png"),
    "trap": pygame.image.load("../assets/trap.png"),
    "cheese": pygame.image.load("../assets/cheese.png")
}

class MouseAndCheeseRender:
    def __init__(self, environment: ndarray):
        self.map_matrix = environment
        pass

    def play(self, path):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        current_index = 0

        while True:
            screen.fill(LIGHTSKYBLUE)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

            mouse = path[current_index]
            traps = list(zip(*np.where(self.map_matrix == 2)))
            cheese = list(zip(*np.where(self.map_matrix == 3)))[0]

            surface = pygame.Surface((TALE_SIZE, TALE_SIZE))
            screen.blit(assets["cheese"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in cheese)[::-1]))
            for trap in traps:
                screen.blit(assets["trap"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in trap)[::-1]))
            screen.blit(assets["mouse"], surface.get_rect(topleft=tuple(x * TALE_SIZE for x in mouse)[::-1]))

            pygame.display.update()
            if current_index + 1 < len(path):
                current_index += 1
            time.sleep(SLEEP_TIME)
