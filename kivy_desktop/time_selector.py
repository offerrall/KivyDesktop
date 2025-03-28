from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.metrics import dp
from kivy.clock import Clock

from .theme import COLORS, METRICS
from .numeric import DNumeric


class DTimeSelector(BoxLayout):
    """
    hours: int \n
    minutes: int \n
    seconds: int \n
    allow_over_24: bool \n
    use_seconds: bool \n
    background_color: list \n
    border_color: list \n
    border_hover: list \n
    border_line_width: int \n
    background_radius: list \n
    text_color: list \n
    on_change_callback: function \n
    """

    hours = NumericProperty(0)
    minutes = NumericProperty(0)
    seconds = NumericProperty(0)
    
    allow_over_24 = BooleanProperty(False)
    use_seconds = BooleanProperty(True)
    
    background_color = ListProperty(COLORS['back2'])
    border_color = ListProperty(COLORS['back2'])
    border_hover = ListProperty(COLORS['seleted'])
    border_line_width = NumericProperty(METRICS['border_line_width'])
    background_radius = ListProperty(METRICS['background_radius'])
    text_color = ListProperty(COLORS['font'])
    
    on_change_callback = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DTimeSelector, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = dp(5)
        
        self.hours_numeric = DNumeric(
            value=self.hours,
            min_value=0,
            max_value=99 if self.allow_over_24 else 23,
            step=1,
            use_float=False,
            on_change_callback=self.on_hours_changed,
            background_color=self.background_color,
            border_color=self.border_color,
            plus_minus_border_color_down=self.border_hover,
            text_color=self.text_color,
            size_hint_x=0.33
        )
        
        self.minutes_numeric = DNumeric(
            value=self.minutes,
            min_value=0,
            max_value=59,
            step=1,
            use_float=False,
            on_change_callback=self.on_minutes_changed,
            background_color=self.background_color,
            border_color=self.border_color,
            plus_minus_border_color_down=self.border_hover,
            text_color=self.text_color,
            size_hint_x=0.33
        )
        
        self.seconds_numeric = DNumeric(
            value=self.seconds,
            min_value=0,
            max_value=59,
            step=1,
            use_float=False,
            on_change_callback=self.on_seconds_changed,
            background_color=self.background_color,
            border_color=self.border_color,
            plus_minus_border_color_down=self.border_hover,
            text_color=self.text_color,
            size_hint_x=0.33
        )
        
        self.add_widget(self.hours_numeric)
        self.add_widget(self.minutes_numeric)
        
        if self.use_seconds:
            self.add_widget(self.seconds_numeric)
        
        self.bind(hours=self.update_hours)
        self.bind(minutes=self.update_minutes)
        self.bind(seconds=self.update_seconds)
        self.bind(allow_over_24=self.update_hours_max)
        self.bind(use_seconds=self.toggle_seconds)
        
    def on_hours_changed(self, instance, value):
        self.hours = value
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def on_minutes_changed(self, instance, value):
        self.minutes = value
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def on_seconds_changed(self, instance, value):
        self.seconds = value
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def update_hours(self, instance, value):
        if value != self.hours_numeric.value:
            self.hours_numeric.value = value
    
    def update_minutes(self, instance, value):
        if value != self.minutes_numeric.value:
            self.minutes_numeric.value = value
    
    def update_seconds(self, instance, value):
        if value != self.seconds_numeric.value:
            self.seconds_numeric.value = value
    
    def update_hours_max(self, instance, value):
        max_value = 99 if value else 23
        self.hours_numeric.max_value = max_value
        if not value and self.hours > 23:
            self.hours = 23
    
    def toggle_seconds(self, instance, value):
        if value and self.seconds_numeric not in self.children:
            self.add_widget(self.seconds_numeric)
        elif not value and self.seconds_numeric in self.children:
            self.remove_widget(self.seconds_numeric)
    
    def get_total_seconds(self):
        """Returns the total time in seconds"""
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def set_time(self, hours=0, minutes=0, seconds=0):
        """Set the time directly"""
        if not self.allow_over_24 and hours > 23:
            hours = 23
        
        if minutes > 59:
            minutes = 59
            
        if seconds > 59:
            seconds = 59
            
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def set_from_seconds(self, total_seconds):
        """Set the time from total seconds"""
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        
        self.set_time(hours, minutes, seconds)