import pygame

from main_menu import main_menu
import os

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

if __name__ == "__main__":
    main_menu()
