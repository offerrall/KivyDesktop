from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.metrics import dp


class Dpopup(Popup):
    """
    title: str \n
    message: str \n
    size: tuple
    """
    def __init__(self,
                 title: str,
                 message: str,
                 size: tuple = (dp(300), dp(100)),
                 **kwargs):
        super(Dpopup, self).__init__(**kwargs)
        self.title = title
        self.content = Label(text=message)
        self.size_hint = (None, None)
        self.size = size
        