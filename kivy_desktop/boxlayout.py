from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy_desktop.theme import COLORS, METRICS
from kivy.properties import NumericProperty



class DBoxLayout(BoxLayout):
    """
    background_color: list \n
    background_radius: list \n
    border_line_width: int \n
    border_color: list \n
    padding: list \n
    orientation: str \n
    """
    background_color = ListProperty(COLORS['back'])
    background_radius = ListProperty(METRICS['background_radius'])
    border_line_width = NumericProperty(METRICS['border_line_width'])
    border_color = ListProperty(COLORS['back2'])
    padding = ListProperty([dp(10), dp(10), dp(10), dp(10)])
    orientation = "vertical"
    
    def __init__(self, **kwargs):
        super(DBoxLayout, self).__init__(**kwargs)