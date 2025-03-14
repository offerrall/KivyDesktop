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

    def __init__(self, **kwargs):
        kwargs.setdefault('size_hint_y', None)
        kwargs.setdefault('height', dp(30))
        kwargs.setdefault('background_radius', [0, 0, 0, 0])
        kwargs.setdefault('content_alignment', 'left')
        super(DSpinnerOption, self).__init__(**kwargs)

class DSpinner(BoxLayout):

    text = StringProperty('')
    values = ListProperty([])
    is_open = BooleanProperty(False)
    is_hover = BooleanProperty(False)
    
    background_color = ListProperty(COLORS['back1'])
    border_color = ListProperty(COLORS['border'])
    border_hover = ListProperty(COLORS['seleted'])
    border_width = NumericProperty(dp(1.2))
    background_color_down = ListProperty(COLORS['back2'])
    text_color = ListProperty(COLORS['font'])
    option_height = NumericProperty(dp(40))
    dropdown_max_height = NumericProperty(dp(200))
    background_radius = ListProperty([dp(6), dp(6), dp(6), dp(6)])
    
    on_select_callback = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(DSpinner, self).__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        
        self.size_hint_y = None
        self.height = dp(40)
        
        self.drop_button = DButton(
            text=self.text or 'Select an option',
            icon_source='./down-arrow.png',
            icon_placement='right',
            icon_size=dp(14),
            border_line_width=self.border_width,
            background_color=self.background_color,
            background_color_down=self.background_color_down,
            border_color=self.border_color,
            border_hover=self.border_hover,
            font_color=self.text_color,
            background_radius=self.background_radius,
            release_callback=self.toggle_dropdown
        )
        self.add_widget(self.drop_button)
        
        self.dropdown = DropDown(
            auto_width=False,
            size_hint=(None, None),
            max_height=self.dropdown_max_height
        )
        self.dropdown.container.padding = [dp(5), dp(5), dp(5), dp(5)]
        self.dropdown.container.spacing = self.border_width * 2
        self.dropdown.bind(on_dismiss=self._on_dropdown_dismiss)
        self.dropdown.bind(on_select=self._on_dropdown_select)
        
        self._update_dropdown_values()
        
        self.bind(text=self._update_button_text)
        self.bind(values=self._update_dropdown_values)
        
    def _update_button_text(self, instance, value):
        if value:
            self.drop_button.text = value
        else:
            self.drop_button.text = 'Select an option'
    

    def _update_dropdown_values(self, *args):
        self.dropdown.clear_widgets()
        
        # Calculate border radius for items
        top_radius = [self.background_radius[0], self.background_radius[1], 0, 0]
        middle_radius = [0, 0, 0, 0]
        bottom_radius = [0, 0, self.background_radius[2], self.background_radius[3]]
        
        for index, value in enumerate(self.values):
            # Determine which radius to use based on position
            if len(self.values) == 1:
                # If only one item, use full radius
                item_radius = self.background_radius
            elif index == 0:
                # First item gets top radius
                item_radius = top_radius
            elif index == len(self.values) - 1:
                # Last item gets bottom radius
                item_radius = bottom_radius
            else:
                # Middle items get no radius
                item_radius = middle_radius
            
            option = DSpinnerOption(
                text=value,
                background_color=self.background_color,
                background_color_down=self.background_color_down,
                border_color=self.border_color,
                border_hover=self.border_hover,
                border_line_width=self.border_width,
                font_color=self.text_color,
                width=self.width,
                background_radius=item_radius
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