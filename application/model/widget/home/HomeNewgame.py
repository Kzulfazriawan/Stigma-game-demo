from library.stigma.application import Button


class HomeNewgame(Button):
    def __init__(self):
        super(HomeNewgame, self).__init__()
        self.text   = 'New game'
        self.params = None