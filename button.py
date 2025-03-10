from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window

class DButton(BoxLayout):
    text = StringProperty('Button')
    is_pressed = BooleanProperty(False)
    is_hover = BooleanProperty(False)
    release_callback = ObjectProperty(None)
    
    background_color = ListProperty([0.10, 0.10, 0.10, 1])
    background_color_down = ListProperty([0.05, 0.05, 0.05, 1])
    border_color = ListProperty([0, 0, 0, 1])
    border_color_down = ListProperty([0, 1, 1, 1])

    background_radius = ListProperty([dp(6), dp(6), dp(6), dp(6)])
    border_line_width = NumericProperty(dp(1.2))
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self.border_color_cache = self.border_color
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.is_pressed = True
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        if self.is_pressed:
            self.is_pressed = False
            self.on_press()
        return super().on_touch_up(touch)
    
    def on_press(self):
        if self.release_callback:
            self.release_callback(self)
    
    def on_mouse_pos(self, window, pos):
        inside = self.collide_point(*self.to_widget(*pos))
        
        if inside != self.is_hover:
            self.is_hover = inside
            self.apply_hover_effect(self.is_hover)
    
    def apply_hover_effect(self, is_hover):
        if is_hover:
            self.border_color_cache = self.border_color.copy()
            r, g, b, a = self.border_color_down
            self.border_color = [r * 0.8, g * 0.8, b * 0.8, a]
        else:
            self.border_color = self.border_color_cache
    
    def on_parent(self, widget, parent):
        if parent is None:
            Window.unbind(mouse_pos=self.on_mouse_pos)