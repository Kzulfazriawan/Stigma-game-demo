from core import Files
from library.stigma.application import Button
from library.stigma.helper import kivyBuilder
kivyBuilder(Files.apppath, 'model', 'builder', 'Buttontwo.kv')


class SerializeButtontri(Button):
    def __init__(self):
        super(SerializeButtontri, self).__init__()
        self.value  = '2'
        self.text  = 'SLOT 3'
        self.data   = None
        self.params = int(self.value)