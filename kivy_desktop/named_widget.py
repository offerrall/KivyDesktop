from kivy_desktop.boxlayout import DBoxLayout
from kivy.metrics import dp
from kivy.uix.label import Label
from kivy.properties import ListProperty, NumericProperty, StringProperty, OptionProperty

class NamedWidget(DBoxLayout):
    orientation = StringProperty("horizontal")
    padding = ListProperty([0, 0, 0, 0])
    name_width = NumericProperty(dp(70))
    text_align = OptionProperty("left", options=["left", "center", "right"])
    
    def __init__(self, name: str, widget, text_align="left", **kwargs):
        super(NamedWidget, self).__init__(**kwargs)
        
        label = Label(
            text=name, 
            size_hint_x=None, 
            width=self.name_width,
            halign=text_align,
            valign='middle'
        )
        
        label.bind(size=label.setter('text_size'))
        self.add_widget(label)
        self.add_widget(widget)
        self.text_align = text_align