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
                 title_align = 'center',
                 size: tuple = (dp(800), dp(100)),
                 auto_open = True,
                 **kwargs):
        super(Dpopup, self).__init__(**kwargs)
        self.title = title
        self.content = Label(text=message)
        self.size_hint = (None, None)
        self.size = size
        self.title_align = title_align
        
        if auto_open:
            self.open()