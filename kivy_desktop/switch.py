from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.clock import Clock

from .theme import COLORS
from .button import DButton

class DSwitch(BoxLayout):
    """
    value: bool \n
    on_text: str \n
    off_text: str \n
    background_color: list \n
    border_color: list \n
    border_hover: list \n
    inactive_opacity: float \n
    border_line_width: int \n
    background_radius: list \n
    spacing: int \n
    on_change_callback: function \n
    """
    
    value = BooleanProperty(False)
    on_text = StringProperty('ON')
    off_text = StringProperty('OFF')
    
    background_color = ListProperty(COLORS['back1'])
    border_color = ListProperty(COLORS['back2'])
    border_hover = ListProperty(COLORS['seleted'])
    inactive_opacity = NumericProperty(0.25)
    border_line_width = NumericProperty(dp(1.2))
    background_radius = ListProperty([dp(6), dp(6), dp(6), dp(6)])
    spacing = NumericProperty(dp(2))
    
    on_change_callback = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        self.size_hint_y = None
        self.height = kwargs.get('height', dp(30))
        
        super(DSwitch, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = self.spacing
        
        self.off_button = DButton(
            text=self.off_text,
            border_line_width=self.border_line_width,
            background_color=self.background_color,
            background_color_down=self.background_color,
            border_color=self.border_color,
            border_hover=self.border_hover,
            font_color=COLORS['font'],
            background_radius=[self.background_radius[0], 0, 0, self.background_radius[3]],
            release_callback=lambda btn: self.set_value(False)
        )
        
        self.on_button = DButton(
            text=self.on_text,
            border_line_width=self.border_line_width,
            background_color=self.background_color,
            background_color_down=self.background_color,
            border_color=self.border_color,
            border_hover=self.border_hover,
            font_color=COLORS['font'],
            background_radius=[0, self.background_radius[1], self.background_radius[2], 0],
            release_callback=lambda btn: self.set_value(True)
        )
        
        self.add_widget(self.off_button)
        self.add_widget(self.on_button)
        
        self.bind(value=self.update_button_states)
        self.bind(on_text=lambda instance, value: setattr(self.on_button, 'text', value))
        self.bind(off_text=lambda instance, value: setattr(self.off_button, 'text', value))
        self.bind(height=self.update_height)
        
        Clock.schedule_once(lambda dt: self.update_button_states(self, self.value), 0)
    
    def update_height(self, instance, height):
        self.height = height
    
    def set_value(self, value):
        if self.value != value:
            self.value = value
            if self.on_change_callback:
                self.on_change_callback(self, value)
    
    def update_button_states(self, instance, value):
        if value:
            self.on_button.border_color = self.border_color
            self.off_button.border_color = self.background_color
            self.on_button.label.opacity = 1
            self.off_button.label.opacity = self.inactive_opacity
        else:
            self.off_button.border_color = self.border_color
            self.on_button.border_color = self.background_color
            self.off_button.label.opacity = 1
            self.on_button.label.opacity = self.inactive_opacity