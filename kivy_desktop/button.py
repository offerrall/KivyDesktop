from kivy.uix.boxlayout import BoxLayout
from kivy.properties import BooleanProperty, ObjectProperty, ListProperty, NumericProperty, StringProperty
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.image import Image
from kivy.uix.label import Label

from .theme import COLORS

class DButton(BoxLayout):
    """
    is_pressed: bool \n
    is_hover: bool \n
    icon_size: int \n
    icon_text_spacing: int \n
    border_line_width: int \n
    text: str \n
    icon_source: str \n
    icon_placement: str \n
    content_alignment: str \n
    background_color: list \n
    background_color_down: list \n
    border_color: list \n
    border_hover: list \n
    font_color: list \n
    background_radius: list \n
    internal_padding: list \n
    release_callback: function \n
    """
    
    is_pressed = BooleanProperty(False)
    is_hover = BooleanProperty(False)
    
    icon_size = NumericProperty(dp(24))
    icon_text_spacing = NumericProperty(dp(10))
    border_line_width = NumericProperty(dp(1.2))

    text = StringProperty('Button')
    icon_source = StringProperty('')
    icon_placement = StringProperty('left')
    content_alignment = StringProperty('center')
    
    background_color = ListProperty(COLORS['back1'])
    background_color_down = ListProperty(COLORS['back2'])
    border_color = ListProperty(COLORS['back2'])
    border_hover = ListProperty(COLORS['seleted'])
    font_color = ListProperty(COLORS['font'])

    background_radius = ListProperty([dp(6), dp(6), dp(6), dp(6)])
    internal_padding = ListProperty([dp(10), dp(10), dp(10), dp(10)])

    release_callback = ObjectProperty(None)
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(mouse_pos=self.on_mouse_pos)
        self.border_color_cache = self.border_color
        self.label = None
        self.icon = None
        
        Clock.schedule_once(self.setup_widgets, 0)

    def setup_widgets(self, dt):
        content_box = self.ids.content_box
        content_box.clear_widgets()
        
        if hasattr(self.ids, 'anchor_layout'):
            anchor_layout = self.ids.anchor_layout
            if self.content_alignment == 'left':
                anchor_layout.anchor_x = 'left'
            elif self.content_alignment == 'right':
                anchor_layout.anchor_x = 'right'
            else:
                anchor_layout.anchor_x = 'center'
        
        if self.text:
            self.label = Label(
                text=self.text,
                size_hint=(None, None),
                size=self.label_texture_size,
                valign='middle',
                color=self.font_color,
                pos_hint={'center_y': 0.5}  
            )
            self.bind(text=self._update_label_text)
        
        if self.icon_source:
            self.icon = Image(
                source=self.icon_source,
                size_hint=(None, None),
                size=(self.icon_size, self.icon_size),
                pos_hint={'center_y': 0.5}
            )
            self.bind(icon_source=self._update_icon_source)
            self.bind(icon_size=self._update_icon_size)
            
            if self.text and self.label:
                if self.icon_placement == 'left':
                    content_box.add_widget(self.icon)
                    content_box.add_widget(self.label)
                else:
                    content_box.add_widget(self.label)
                    content_box.add_widget(self.icon)
            else:
                content_box.add_widget(self.icon)
        elif self.text and self.label:
            content_box.add_widget(self.label)
        
        self.bind(icon_placement=self._update_widget_order)
        self.bind(content_alignment=self._update_content_alignment)
        
    def _update_content_alignment(self, instance, value):
        if hasattr(self.ids, 'anchor_layout'):
            if value == 'left':
                self.ids.anchor_layout.anchor_x = 'left'
            elif value == 'right':
                self.ids.anchor_layout.anchor_x = 'right'
            else:
                self.ids.anchor_layout.anchor_x = 'center'
    
    def _update_label_text(self, instance, value):
        content_box = self.ids.content_box
        
        if not value and self.label:
            if self.label in content_box.children:
                content_box.remove_widget(self.label)
            self.label = None
            self._update_widget_order(self, self.icon_placement)
            return
            
        if value and not self.label:
            self.label = Label(
                text=value,
                size_hint=(None, None),
                size=self._get_label_size(value),
                valign='middle',
                pos_hint={'center_y': 0.5}
            )
            self._update_widget_order(self, self.icon_placement)

        elif value and self.label:
            self.label.text = value
            self.label.texture_update()
            self.label.size = self.label.texture_size
    
    def _update_icon_source(self, instance, value):
        if not value and self.icon and hasattr(self, 'ids') and hasattr(self.ids, 'content_box'):
            content_box = self.ids.content_box
            if self.icon in content_box.children:
                content_box.remove_widget(self.icon)
            self.icon = None
            self._update_widget_order(self, self.icon_placement)
        elif value:
            if not self.icon:
                self.icon = Image(
                    source=value,
                    size_hint=(None, None),
                    size=(self.icon_size, self.icon_size),
                    pos_hint={'center_y': 0.5}
                )
                self._update_widget_order(self, self.icon_placement)
            else:
                self.icon.source = value
                self.icon.opacity = 1
                self.icon.size = (self.icon_size, self.icon_size)
    
    def _update_icon_size(self, instance, value):
        if self.icon and self.icon_source:
            self.icon.size = (value, value)
    
    def _update_widget_order(self, instance, value):
        if hasattr(self, 'ids') and hasattr(self.ids, 'content_box'):
            content_box = self.ids.content_box
            content_box.clear_widgets()
            
            has_icon = hasattr(self, 'icon') and self.icon is not None
            has_label = hasattr(self, 'label') and self.label is not None
            
            if has_icon and has_label:
                if value == 'left':
                    content_box.add_widget(self.icon)
                    content_box.add_widget(self.label)
                else:
                    content_box.add_widget(self.label)
                    content_box.add_widget(self.icon)
            elif has_icon:
                content_box.add_widget(self.icon)
            elif has_label:
                content_box.add_widget(self.label)
    
    def _get_label_size(self, text):
        label = Label(text=text)
        label.texture_update()
        return label.texture_size
        
    @property
    def label_texture_size(self):
        if not self.text:
            return (0, 0)
        label = Label(text=self.text)
        label.texture_update()
        return label.texture_size
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.is_pressed = True
        return super().on_touch_down(touch)
    
    def on_touch_up(self, touch):
        was_pressed = self.is_pressed
        if was_pressed and self.collide_point(*touch.pos):
            self.is_pressed = False
            self.on_press()
        elif was_pressed:
            self.is_pressed = False
        return super().on_touch_up(touch)
    
    def on_press(self):
        if self.release_callback:
            self.release_callback(self)
    
    def on_mouse_pos(self, window, pos):
        inside = self.collide_point(*self.to_widget(*pos))
        
        if inside != self.is_hover:
            self.is_hover = inside
    
    def on_parent(self, widget, parent):
        if parent is None:
            Window.unbind(mouse_pos=self.on_mouse_pos)