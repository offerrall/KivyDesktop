from kivy.uix.boxlayout import BoxLayout
from kivy.metrics import dp
from kivy.properties import ListProperty
from kivy_desktop.theme import COLORS



class DBoxLayout(BoxLayout):
    background_color = ListProperty(COLORS['back'])
    padding = ListProperty([dp(10), dp(10), dp(10), dp(10)])
    orientation = "vertical"
    
    def __init__(self, **kwargs):
        super(DBoxLayout, self).__init__(**kwargs)