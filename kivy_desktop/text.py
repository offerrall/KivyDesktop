from kivy.uix.textinput import TextInput
from kivy.properties import ListProperty, StringProperty, BooleanProperty


class DTextInput(TextInput):
    """
    background_normal: str \n
    background_active: str \n
    background_color: list \n
    cursor_color: list \n
    multiline: bool \n
    """
    background_normal = StringProperty("")
    background_active = StringProperty("")
    foreground_color = ListProperty([1, 1, 1, 1])
    background_color = ListProperty([0, 0, 0, 0])
    cursor_color = ListProperty([1, 1, 1, 1])
    multiline = BooleanProperty(False)
    
    def __init__(self, **kwargs):
        super(DTextInput, self).__init__(**kwargs)