from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, NumericProperty, BooleanProperty
from kivy.metrics import dp

class DScrollView(ScrollView):

    orientation = ObjectProperty('vertical')
    spacing = NumericProperty(dp(10))
    padding = NumericProperty(dp(10))
    auto_adjust_height = BooleanProperty(True)
    
    def __init__(self, **kwargs):
        kwargs.setdefault('size_hint', (1, 1))
        kwargs.setdefault('do_scroll_x', False)
        kwargs.setdefault('effect_cls', 'ScrollEffect')
        
        orientation = kwargs.pop('orientation', 'vertical')
        spacing = kwargs.pop('spacing', dp(10))
        padding = kwargs.pop('padding', dp(10))
        self.auto_adjust_height = kwargs.pop('auto_adjust_height', True)
        
        super(DScrollView, self).__init__(**kwargs)
        
        self.layout = BoxLayout(
            orientation=orientation,
            spacing=spacing,
            padding=padding,
            size_hint_y=None if orientation == 'vertical' else 1,
            size_hint_x=None if orientation == 'horizontal' else 1
        )
        
        if orientation == 'vertical' and self.auto_adjust_height:
            self.layout.bind(minimum_height=self.layout.setter('height'))
        elif orientation == 'horizontal' and self.auto_adjust_height:
            self.layout.bind(minimum_width=self.layout.setter('width'))
        
        self.add_widget(self.layout)
    
    def add_widget(self, widget, index=0, *args, **kwargs):

        if len(self.children) < 1 or widget == self.layout:
            super(DScrollView, self).add_widget(widget, index, *args, **kwargs)
        else:
            self.layout.add_widget(widget, index, *args, **kwargs)
    
    def remove_widget(self, widget, *args, **kwargs):

        if widget == self.layout:
            super(DScrollView, self).remove_widget(widget, *args, **kwargs)
        else:
            self.layout.remove_widget(widget, *args, **kwargs)
    
    def clear_widgets(self, children=None):

        self.layout.clear_widgets(children)