from kivy_desktop.boxlayout import DBoxLayout
from kivy.metrics import dp

from kivy.uix.label import Label

from kivy.properties import ListProperty, NumericProperty, StringProperty

class NamedWidget(DBoxLayout):
    orientation = StringProperty("horizontal")
    padding = ListProperty([0, 0, 0, 0])
    name_width = NumericProperty(dp(70))
    
    def __init__(self, name: str, widget, **kwargs):
        super(NamedWidget, self).__init__(**kwargs)
        self.add_widget(Label(text=name, size_hint_x=None, width=self.name_width))
        self.add_widget(widget)