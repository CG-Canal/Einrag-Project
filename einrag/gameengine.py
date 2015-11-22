from utils.desctype import Desctype


class GameEngine:
    def __init__(self, game_gui, world_yaml, char_yaml):
        self.game_gui = game_gui

        self.world_yaml = world_yaml
        self.char_yaml = char_yaml

        self.game_gui.input.returnPressed.connect(self.eventInputEnterPressed)

    def loop():
        self.show_desc(Desctype.world)

        while True:
            user_input = input()


    def eventInputEnterPressed(self):
        #self.game_gui.addText(self.game_gui.input.text() + "\n", (250, 250, 250))

        # Do something
        self.game_gui.input.setText("")


    def show_desc(self, what_desc):
        if isinstance(what_desc, Desctype):
            print(self.world_yaml[str(self.get_char_posx()) + "," +
                                  str(self.get_char_posy())]['desc'])


    def get_char_posx(self):
        x = self.char_yaml['pos']['x']
        return x


    def get_char_posy(self):
        y = self.char_yaml['pos']['y']
        return y
