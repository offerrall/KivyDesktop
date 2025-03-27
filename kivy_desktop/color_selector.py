from kivy.uix.widget import Widget
from kivy.properties import ListProperty, ObjectProperty
from .theme import METRICS

from kivy.uix.modalview import ModalView
from kivy.uix.colorpicker import ColorPicker

from .boxlayout import DBoxLayout


class DColorSelector(Widget):
    """
    color: list \n
    background_radius: list \n
    color_change_callback: function \n
    """
    color = ListProperty([1, 1, 1, 1])
    background_radius = ListProperty(METRICS['background_radius'])
    color_change_callback = ObjectProperty(None)
    
    def __init__(self,
                 **kwargs):
        super(DColorSelector, self).__init__(**kwargs)
    
    
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            
            modal = ModalView(size_hint=(None, None), size=(400, 400), background_color=[0, 0, 0, 0], background='')
            lay = DBoxLayout()
            lay.orientation = "vertical"
            
            color_picker = ColorPicker()
            color_picker.bind(color=self.change_color)
            color_picker.color = self.color
            lay.add_widget(color_picker)
            
            modal.add_widget(lay)
            modal.open()
            
            return True
        return super(DColorSelector, self).on_touch_down(touch)
    
    def change_color(self, instance, value):
        self.color = value
        if self.color_change_callback:
            self.color_change_callback(self.color)
        return self.color