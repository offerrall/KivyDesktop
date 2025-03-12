from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import NumericProperty, StringProperty, ObjectProperty
from kivy.metrics import dp
from kivy.clock import Clock

from kivy_desktop.button import DButton

class DInt(BoxLayout):

    value = NumericProperty(0)
    min_value = NumericProperty(-99999)
    max_value = NumericProperty(99999)
    step = NumericProperty(1)
    
    hint_text = StringProperty("")
    validation_message = StringProperty("")
    
    on_change_callback = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DInt, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.spacing = dp(0)
        self.size_hint_y = None
        self.height = dp(40)
        
        self.decrement_btn = DButton(
            text="-",
            size_hint=(None, 1),
            width=dp(40),
            release_callback=self.decrement,
            background_radius=[dp(6), 0, 0, dp(6)]
        )
        
        self.text_input = TextInput(
            text=str(self.value),
            multiline=False,
            halign='center',
            size_hint=(1, 1),
            input_filter='int',
            background_color=[0.12, 0.14, 0.17, 1],
            foreground_color=[1, 1, 1, 1],
            cursor_color=[1, 1, 1, 1],
            padding=[dp(10), dp(10), 0, 0]
        )
        
        self.increment_btn = DButton(
            text="+",
            size_hint=(None, 1),
            width=dp(40),
            release_callback=self.increment,
            background_radius=[0, dp(6), dp(6), 0]
        )
        
        self.add_widget(self.decrement_btn)
        self.add_widget(self.text_input)
        self.add_widget(self.increment_btn)
        
        self.text_input.bind(text=self.on_text_changed)
        self.bind(value=self.on_value_changed)
        self.bind(min_value=self.update_buttons_state)
        self.bind(max_value=self.update_buttons_state)
        
        Clock.schedule_once(self.update_buttons_state, 0)
    
    def increment(self, instance):

        new_value = self.value + self.step
        if new_value <= self.max_value:
            self.value = new_value
    
    def decrement(self, instance):

        new_value = self.value - self.step
        if new_value >= self.min_value:
            self.value = new_value
    
    def on_text_changed(self, instance, text):

        if text == '':
            return
        
        try:
            value = int(text)
            if self.min_value <= value <= self.max_value:
                if value != self.value:
                    self.value = value
            else:

                Clock.schedule_once(lambda dt: setattr(self.text_input, 'text', str(self.value)), 0)
        except ValueError:

            Clock.schedule_once(lambda dt: setattr(self.text_input, 'text', str(self.value)), 0)
    
    def on_value_changed(self, instance, value):

        if self.text_input.text != str(value):
            self.text_input.text = str(value)
        
        self.update_buttons_state()
        
        if self.on_change_callback:
            self.on_change_callback(self, value)
    
    def update_buttons_state(self, *args):

        self.decrement_btn.disabled = self.value <= self.min_value
        self.increment_btn.disabled = self.value >= self.max_value
        
        if hasattr(self.decrement_btn, 'opacity'):
            self.decrement_btn.opacity = 0.5 if self.decrement_btn.disabled else 1.0
        if hasattr(self.increment_btn, 'opacity'):
            self.increment_btn.opacity = 0.5 if self.increment_btn.disabled else 1.0