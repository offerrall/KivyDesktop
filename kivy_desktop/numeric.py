from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, ObjectProperty, ListProperty, BooleanProperty
from kivy.metrics import dp
from kivy.clock import Clock
from kivy.core.window import Window

from .theme import COLORS, METRICS
from .state import STATE
from .button import DButton

class DNumeric(BoxLayout):
    """
    value: int \n
    min_value: int \n
    max_value: int \n
    step: int \n
    use_float: bool \n
    float_precision: int \n
    background_radius: int \n
    border_line_width: int \n
    plus_minus_width: int \n
    background_color: list \n
    border_color: list \n
    text_color: list \n
    plus_minus_border_color_down: list \n
    error_color: list \n
    plus_minus_background_color: list \n
    on_change_callback: function \n
    is_dragging: bool \n
    is_hover: bool \n
    drag_sensitivity: float \n
    """

    value = NumericProperty(0)
    min_value = NumericProperty(-99999)
    max_value = NumericProperty(99999)
    step = NumericProperty(1)
    
    use_float = BooleanProperty(False)
    float_precision = NumericProperty(2)

    background_radius = NumericProperty(METRICS['background_radius'][0])
    border_line_width = NumericProperty(METRICS['border_line_width'])
    plus_minus_width = NumericProperty(dp(40))

    background_color = ListProperty(COLORS['back2'])
    border_color = ListProperty(COLORS['back2'])
    text_color = ListProperty(COLORS['font'])
    plus_minus_border_color_down = ListProperty(COLORS['seleted'])
    error_color = ListProperty(COLORS['error'])
    plus_minus_background_color = ListProperty(COLORS['back1'])
    
    on_change_callback = ObjectProperty(None)
    
    is_dragging = BooleanProperty(False)
    is_hover = BooleanProperty(False)
    drag_sensitivity = NumericProperty(0.1)
    
    def __init__(self, **kwargs):
        super(DNumeric, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = dp(0)
        
        if self.value < self.min_value:
            self.value = self.min_value
        
        if self.value > self.max_value:
            self.value = self.max_value
        
        self.decrement_error_timer = None
        self.increment_error_timer = None
        
        self.drag_start_x = 0
        self.drag_start_value = 0
        self.drag_active = False
        self.drag_touch_id = None
        
        self.decrement_btn = DButton(
            text="-",
            size_hint_x=None,
            width=self.plus_minus_width,
            border_color=self.border_color,
            border_hover=self.plus_minus_border_color_down,
            release_callback=self.decrement,
            border_line_width=self.border_line_width,
            background_color=self.plus_minus_background_color,
            background_color_down=self.background_color,
            font_color=self.text_color,
            background_radius=[self.background_radius, 0, 0, self.background_radius]
        )
        
        self.text_input = TextInput(
            text=self.format_value(self.value),
            multiline=False,
            halign='center',
            background_normal='',
            background_active='',
            border=[0, 0, 0, 0],
            background_color=[0, 0, 0, 0],
            foreground_color=self.text_color,
            cursor_color=[1, 1, 1, 1],
        )
        
        self.increment_btn = DButton(
            text="+",
            size_hint_x=None,
            width=self.plus_minus_width,
            border_color=self.border_color,
            border_hover=self.plus_minus_border_color_down,
            release_callback=self.increment,
            border_line_width=self.border_line_width,
            background_color=self.plus_minus_background_color,
            background_color_down=self.background_color,
            font_color=self.text_color,
            background_radius=[0, self.background_radius, self.background_radius, 0]
        )
        
        self.add_widget(self.decrement_btn)
        self.add_widget(self.text_input)
        self.add_widget(self.increment_btn)
        
        self.text_input.bind(text=self.on_text_changed)
        self.bind(value=self.on_value_changed)
        self.bind(min_value=self.update_buttons_state)
        self.bind(max_value=self.update_buttons_state)
        self.bind(float_precision=self.on_float_precision_changed)
        self.bind(use_float=self.on_use_float_changed)
        
        Window.bind(mouse_pos=self.on_mouse_move)
        Window.bind(on_touch_down=self.on_window_touch_down)
        Window.bind(on_touch_move=self.on_window_touch_move)
        Window.bind(on_touch_up=self.on_window_touch_up)
        
        Clock.schedule_once(self.update_buttons_state, 0)
        Clock.schedule_once(self.center_text_vertically, 0)

    def format_value(self, value):
        if self.use_float:
            format_str = f"{{:.{self.float_precision}f}}"
            return format_str.format(value)
        else:
            return str(int(value))
            
    def on_float_precision_changed(self, instance, float_precision):
        if self.use_float:
            self.text_input.text = self.format_value(self.value)
            
    def on_use_float_changed(self, instance, use_float):
        self.text_input.text = self.format_value(self.value)

    def center_text_vertically(self, dt):
        available_space = self.text_input.height - self.text_input.minimum_height
        
        offset = dp(7)
        
        top_padding = (available_space / 2.0) + offset
        bottom_padding = (available_space / 2.0) - offset
        
        self.text_input.padding_y = [top_padding, bottom_padding]
        self.text_input.bind(height=self.on_text_input_height_changed)
        
    def on_text_input_height_changed(self, instance, height):
        self.center_text_vertically(0)

    def increment(self, instance):
        new_value = self.value + self.step
        if new_value <= self.max_value:
            self.value = new_value
        else:
            self.set_increment_error_state()
    
    def decrement(self, instance):
        new_value = self.value - self.step
        if new_value >= self.min_value:
            self.value = new_value
        else:
            self.set_decrement_error_state()
    
    def set_increment_error_state(self):
        if self.increment_error_timer:
            self.increment_error_timer.cancel()

        self.increment_btn.border_hover = self.error_color
        self.increment_btn.border_color = self.error_color
        
        self.increment_error_timer = Clock.schedule_once(self.reset_increment_state, 0.2)
    
    def set_decrement_error_state(self):
        if self.decrement_error_timer:
            self.decrement_error_timer.cancel()

        self.decrement_btn.border_hover = self.error_color
        self.decrement_btn.border_color = self.error_color

        self.decrement_error_timer = Clock.schedule_once(self.reset_decrement_state, 0.2)
    
    def reset_increment_state(self, dt):
        self.increment_btn.border_hover = self.plus_minus_border_color_down
        self.increment_btn.border_color = self.border_color
        self.increment_error_timer = None
    
    def reset_decrement_state(self, dt):
        self.decrement_btn.border_hover = self.plus_minus_border_color_down
        self.decrement_btn.border_color = self.border_color
        self.decrement_error_timer = None
    
    def on_text_changed(self, instance, text):
        if text == '':
            return
        if text == '-':
            return
        if self.use_float and text.count('.') == 1 and text.endswith('.'):
            return
            
        try:
            if self.use_float:
                value = float(text)
            else:
                value = int(text)
                
            if self.min_value <= value <= self.max_value:
                if value != self.value:
                    self.value = value
            else:
                Clock.schedule_once(lambda dt: setattr(self.text_input, 'text', self.format_value(self.value)), 0)
        except ValueError:
            Clock.schedule_once(lambda dt: setattr(self.text_input, 'text', self.format_value(self.value)), 0)
    
    def on_value_changed(self, instance, value):
        formatted_value = self.format_value(value)
        if self.text_input.text != formatted_value:
            self.text_input.text = formatted_value
        
        if self.on_change_callback:
            self.on_change_callback(self, value)
    
    def update_buttons_state(self, *args):
        decrement_disabled = self.value <= self.min_value
        increment_disabled = self.value >= self.max_value

        if self.decrement_error_timer:
            if not decrement_disabled:
                self.decrement_btn.border_hover = self.plus_minus_border_color_down
                self.decrement_btn.border_color = self.border_color
                self.decrement_error_timer.cancel()
                self.decrement_error_timer = None
        
        if self.increment_error_timer:
            if not increment_disabled:
                self.increment_btn.border_hover = self.plus_minus_border_color_down
                self.increment_btn.border_color = self.border_color
                self.increment_error_timer.cancel()
                self.increment_error_timer = None
    
    def on_window_touch_down(self, window, touch):
        if STATE.drop_menu_open:
            return False

        if hasattr(touch, 'button') and touch.button.startswith('scroll'):
            return False
        
        if self.text_input.collide_point(*self.text_input.to_widget(*touch.pos)):
            if touch.is_double_tap:
                Window.set_system_cursor('ibeam')
                return False
            else:
                self.start_drag(touch)
                return True
        
        return False
    
    def start_drag(self, touch):
        self.drag_touch_id = touch.uid
        
        self.text_input.readonly = True
        
        Window.set_system_cursor('size_we')
        
        self.drag_start_x = touch.x
        self.drag_start_value = self.value
        self.drag_active = True
        self.is_dragging = True
    
    def on_window_touch_move(self, window, touch):

        if STATE.drop_menu_open:
            return False

        if self.drag_active and touch.uid == self.drag_touch_id:
            delta_x = touch.x - self.drag_start_x
            
            if self.use_float:
                sensitivity_factor = 10 * self.step if self.step >= 1 else 1
                delta_value = (delta_x / (dp(10) * self.drag_sensitivity)) * self.step / sensitivity_factor
                new_value = self.drag_start_value + delta_value
            else:
                delta_value = int(delta_x / (dp(10) * self.drag_sensitivity))
                new_value = self.drag_start_value + delta_value
            
            new_value = max(self.min_value, min(new_value, self.max_value))
            
            if new_value != self.value:
                self.value = new_value
    
    def on_window_touch_up(self, window, touch):

        if self.drag_active and touch.uid == self.drag_touch_id:
            self.drag_active = False
            self.is_dragging = False
            self.drag_touch_id = None
            
            self.text_input.readonly = False
            
            if not self.is_hover:
                Window.set_system_cursor('arrow')
            
            if abs(touch.x - self.drag_start_x) < dp(3):
                self.text_input.focus = True
    
    def on_mouse_move(self, window, pos):
        if STATE.drop_menu_open:
            return False
        widget_pos = self.to_widget(*pos)
        
        if self.text_input.collide_point(*self.text_input.to_widget(*pos)):
            Window.set_system_cursor('size_we')
            self.is_hover = True
        else:
            if self.is_hover and not self.drag_active:
                Window.set_system_cursor('arrow')
                self.is_hover = False
        
        if self.drag_active:
            x, y = self.to_widget(*pos)
            delta_x = x - self.drag_start_x
            
            if self.use_float:
                sensitivity_factor = 10 * self.step if self.step >= 1 else 1
                delta_value = (delta_x / (dp(10) * self.drag_sensitivity)) * self.step / sensitivity_factor
                new_value = self.drag_start_value + delta_value
            else:
                delta_value = int(delta_x / (dp(10) * self.drag_sensitivity))
                new_value = self.drag_start_value + delta_value
            
            new_value = max(self.min_value, min(new_value, self.max_value))
            
            if new_value != self.value:
                self.value = new_value
    
    def on_parent(self, widget, parent):
        if parent is None:

            Window.unbind(mouse_pos=self.on_mouse_move)
            Window.unbind(on_touch_down=self.on_window_touch_down)
            Window.unbind(on_touch_move=self.on_window_touch_move)
            Window.unbind(on_touch_up=self.on_window_touch_up)