from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.clock import Clock

from .button import DButton
from .theme import COLORS

class DSpinnerOption(DButton):
    """Widget for each option in the dropdown"""
    
    def __init__(self, **kwargs):
        kwargs.setdefault('size_hint_y', None)
        kwargs.setdefault('height', dp(30))
        kwargs.setdefault('background_radius', [0, 0, 0, 0])
        kwargs.setdefault('content_alignment', 'left')
        super(DSpinnerOption, self).__init__(**kwargs)

class DSpinner(BoxLayout):
    """Custom Spinner widget that allows selecting from a dropdown list"""
    text = StringProperty('')
    values = ListProperty([])
    is_open = BooleanProperty(False)
    is_hover = BooleanProperty(False)
    
    # Styling properties
    background_color = ListProperty(COLORS['back1'])
    border_color = ListProperty(COLORS['border'])
    border_hover = ListProperty(COLORS['seleted'])
    text_color = ListProperty(COLORS['font'])
    option_height = NumericProperty(dp(40))
    dropdown_max_height = NumericProperty(dp(200))
    background_radius = ListProperty([dp(6), dp(6), dp(6), dp(6)])
    
    # Callbacks
    on_select_callback = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DSpinner, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        
        # Default size hint and values
        self.size_hint_y = None
        self.height = dp(40)
        
        # Create the main button
        self.drop_button = DButton(
            text=self.text or 'Select an option',
            icon_source='./down-arrow.png',  # Make sure this file exists
            icon_placement='right',
            icon_size=dp(14),
            background_color=self.background_color,
            border_color=self.border_color,
            border_hover=self.border_hover,
            font_color=self.text_color,
            background_radius=self.background_radius,
            release_callback=self.toggle_dropdown
        )
        self.add_widget(self.drop_button)
        
        # Initialize the dropdown
        self.dropdown = DropDown(
            auto_width=False,
            size_hint=(None, None),
            max_height=self.dropdown_max_height
        )
        self.dropdown.bind(on_dismiss=self._on_dropdown_dismiss)
        self.dropdown.bind(on_select=self._on_dropdown_select)
        
        # Create the dropdown options
        self._update_dropdown_values()
        
        # Bind property changes
        self.bind(text=self._update_button_text)
        self.bind(values=self._update_dropdown_values)
        
    def _update_button_text(self, instance, value):
        if value:
            self.drop_button.text = value
        else:
            self.drop_button.text = 'Select an option'
    
    def _update_dropdown_values(self, *args):
        self.dropdown.clear_widgets()
        
        for value in self.values:
            option = DSpinnerOption(
                text=value,
                background_color=self.background_color,
                font_color=self.text_color,
                width=self.width
            )
            
            # Using a lambda with default argument to avoid late binding issue
            option.release_callback = lambda btn, value=value: self.dropdown.select(value)
            
            self.dropdown.add_widget(option)
    
    def on_mouse_pos(self, window, pos):
        inside = self.collide_point(*self.to_widget(*pos))
        
        if inside != self.is_hover:
            self.is_hover = inside
    
    def toggle_dropdown(self, instance):
        if self.is_open:
            self.dropdown.dismiss()
        else:
            self.open_dropdown()
    
    def open_dropdown(self):
        if not self.values:
            return
        
        # Set the width of the dropdown to match the spinner width
        self.dropdown.width = self.width
        
        # Update option button widths
        for child in self.dropdown.container.children:
            if isinstance(child, DSpinnerOption):
                child.width = self.width
        
        # Open the dropdown
        self.dropdown.open(self.drop_button)
        self.is_open = True
    
    def _on_dropdown_dismiss(self, *args):
        self.is_open = False
    
    def _on_dropdown_select(self, instance, value):
        self.text = value
        if self.on_select_callback:
            self.on_select_callback(value)
            
    def on_parent(self, widget, parent):
        if parent is None:
            Window.unbind(mouse_pos=self.on_mouse_pos)
            
    def set_value(self, value):
        """Programmatically set the spinner value"""
        if value in self.values:
            self.text = value
            if self.on_select_callback:
                self.on_select_callback(value)