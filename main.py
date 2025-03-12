from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy_desktop.button import DButton
from kivy_desktop.int import DInt
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class BackgroundWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.25, 0.25, 0.25, 1)  # Rojo (R=1, G=0, B=0, A=1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_rect, size=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


background = BackgroundWidget(orientation='vertical')
scroll_view = DScrollView(size_hint=(1, 1))
scroll_view.layout.padding = [dp(20), dp(20), dp(20), dp(20)]


for i in range(10):
    if i < 2:
        continue
    
    HEIGHT = dp(i * 10)
    print(HEIGHT)
    
    btn = DButton(
        text=f"Height: {HEIGHT}",
        size_hint_y=None,
        size_hint_x=1,
        height=HEIGHT,
        release_callback=lambda instance: print(instance.text)
    )
    
    int_input = DInt(
        size_hint_y=None,
        size_hint_x=1,
        height=HEIGHT,
        min_value=-10,
        max_value=1000,
        value=5,
        border_line_width=dp(1.2),
    )
    
    int_input.bind(value=lambda instance, value: print(value))

    scroll_view.add_widget(btn)
    scroll_view.add_widget(int_input)

background.add_widget(scroll_view)

app = DApp(main_container=background, fps=144, title="Kivy Desktop Test")

if __name__ == "__main__":
    app.run()