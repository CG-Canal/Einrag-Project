from PyQt5.QtWidgets import QApplication
import sys

import yaml

from src.gamegui import GameGui
from src.gameengine import GameEngine

print("[PROG] Program started")


print("[PROG] Initializing the GUI")
app = QApplication(sys.argv)
game_gui = GameGui()


print("[PROG] Initializing the game engine")
world_yaml = 0
char_yaml = 0

with open("./data/esrpg.world", 'r') as stream:
    world_yaml = yaml.load(stream)

with open("./data/eyal.char", 'r') as stream:
    char_yaml = yaml.load(stream)

game_engine = GameEngine(game_gui, world_yaml, char_yaml)


print("[PROG] Starting the GUI")
sys.exit(app.exec_())


print("[PROG] Starting the game engine")
game_engine.loop()


print("[PROG] Program stopping")
