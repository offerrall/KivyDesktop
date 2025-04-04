from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy_desktop.button import DButton
from kivy_desktop.numeric import DNumeric
from kivy_desktop.scroll import DScrollView
from kivy_desktop.spinner import DSpinner
from kivy_desktop.app import DApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
import random

from kivy_desktop.switch import DSwitch

class BackgroundWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.25, 0.25, 0.25, 1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_rect, size=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


background = BackgroundWidget(orientation='vertical')
scroll_view = DScrollView(size_hint=(1, 1))
scroll_view.layout.padding = [dp(20), dp(20), dp(20), dp(20)]

HEIGHT = dp(30)

btn = DButton(
    text=f"Height: {HEIGHT}",
    size_hint_y=None,
    size_hint_x=1,
    height=HEIGHT,
    release_callback=lambda instance: print(instance.text)
)

int_input = DNumeric(
    size_hint_y=None,
    size_hint_x=1,
    height=HEIGHT,
    min_value=-10,
    max_value=1000,
    value=5,
    use_float=bool(random.randint(0, 1)),
    border_line_width=dp(1.2),
)

dropdown = DSpinner(
    size_hint_y=None,
    values=[f"Option {i}" for i in range(5)],
    size_hint_x=1,
    height=HEIGHT,
)

custom_switch = DSwitch(
    value=True,
    size_hint_y=None,
    size_hint_x=1,
    height=HEIGHT,
    on_change_callback=lambda instance, value: print(f"Valor cambiado: {value}")
)

intnumeric = DNumeric(
    size_hint_y=None,
    size_hint_x=1,
    height=dp(100),
    min_value=-10,
    max_value=1000,
    value=5,
    use_float=bool(random.randint(0, 1)),
    border_line_width=dp(1.2),
    on_change_callback=lambda instance, value: print(f"Valor cambiado: {value}")
)


int_input.bind(value=lambda instance, value: print(value))

scroll_view.add_widget(intnumeric)
scroll_view.add_widget(dropdown)
scroll_view.add_widget(btn)
scroll_view.add_widget(int_input)
scroll_view.add_widget(custom_switch)


background.add_widget(scroll_view)

app = DApp(main_container=background, title="Kivy Desktop Test")

if __name__ == "__main__":
    app.run()