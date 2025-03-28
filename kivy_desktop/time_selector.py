from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty
from kivy.metrics import dp

from .theme import COLORS, METRICS
from .numeric import DNumeric


class DTimeSelector(BoxLayout):
    """
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
        initial_hours = kwargs.pop('hours', 0)
        initial_minutes = kwargs.pop('minutes', 0)
        initial_seconds = kwargs.pop('seconds', 0)
        
        super(DTimeSelector, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = dp(5)
        
        self.hours_numeric = DNumeric(
            value=initial_hours,
            min_value=0,
            max_value=99 if self.allow_over_24 else 23,
            step=1,
            use_float=False,
            on_change_callback=self._on_change,
            background_color=self.background_color,
            border_color=self.border_color,
            plus_minus_border_color_down=self.border_hover,
            text_color=self.text_color,
            size_hint_x=0.33
        )
        
        self.minutes_numeric = DNumeric(
            value=initial_minutes,
            min_value=0,
            max_value=59,
            step=1,
            use_float=False,
            on_change_callback=self._on_change,
            background_color=self.background_color,
            border_color=self.border_color,
            plus_minus_border_color_down=self.border_hover,
            text_color=self.text_color,
            size_hint_x=0.33
        )
        
        self.seconds_numeric = DNumeric(
            value=initial_seconds,
            min_value=0,
            max_value=59,
            step=1,
            use_float=False,
            on_change_callback=self._on_change,
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
        
        self.bind(allow_over_24=self._update_hours_max)
        self.bind(use_seconds=self._toggle_seconds)
    
    def _on_change(self, instance, value):
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def _update_hours_max(self, instance, value):
        max_value = 99 if value else 23
        self.hours_numeric.max_value = max_value
        if not value and self.hours_numeric.value > 23:
            self.hours_numeric.value = 23
    
    def _toggle_seconds(self, instance, value):
        if value and self.seconds_numeric not in self.children:
            self.add_widget(self.seconds_numeric)
        elif not value and self.seconds_numeric in self.children:
            self.remove_widget(self.seconds_numeric)
    
    @property
    def hours(self):
        return int(self.hours_numeric.value)
    
    @property
    def minutes(self):
        return int(self.minutes_numeric.value)
    
    @property
    def seconds(self):
        return int(self.seconds_numeric.value)
    
    def get_total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds
    
    def set_time(self, hours=0, minutes=0, seconds=0):
        if not self.allow_over_24 and hours > 23:
            hours = 23
        
        if minutes > 59:
            minutes = 59
            
        if seconds > 59:
            seconds = 59
        
        self.hours_numeric.value = int(hours)
        self.minutes_numeric.value = int(minutes)
        self.seconds_numeric.value = int(seconds)
        
        if self.on_change_callback:
            self.on_change_callback(self)
    
    def set_from_seconds(self, total_seconds):
        if total_seconds < 0:
            total_seconds = 0
            
        hours = total_seconds // 3600
        remaining = total_seconds % 3600
        minutes = remaining // 60
        seconds = remaining % 60
        
        self.set_time(hours, minutes, seconds)