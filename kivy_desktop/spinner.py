from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window

from .button import DButton

from .theme import COLORS

class DSpinner(BoxLayout):
    
    is_hover = BooleanProperty(False)
    background_color = ListProperty(COLORS['back1'])
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)

        self.drop_button = DButton(
            text='Dropdown',
            icon_source='./down-arrow.png',
            icon_placement='right',
            icon_size=dp(16),
            background_color=self.background_color,
            release_callback=self.toggle_dropdown
        )

        self.add_widget(self.drop_button)

    def on_mouse_pos(self, *args):
        self.is_hover = self.collide_point(*Window.mouse_pos)

    def toggle_dropdown(self, instance):
        print('Dropdown pressed')