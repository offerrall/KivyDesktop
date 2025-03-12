from kivy.app import App
from kivy.clock import Clock

class DApp(App):

    def __init__(self,
                 main_container,
                 fps=60,
                 title="Kivy Desktop App",
                 **kwargs):

        self.container = main_container
        self.fps = fps
        kwargs['title'] = title
        super(DApp, self).__init__(**kwargs)
        
        self._update_event = None

    def build(self):
        return self.container
    
    def on_start(self):
        return
        self._update_event = Clock.schedule_interval(self._force_update, 1/self.fps)
    
    def on_stop(self):
        if self._update_event:
            self._update_event.cancel()
    
    def _force_update(self, dt):
        if self.root:
            self.root.canvas.ask_update()
            
            def update_canvas(widget):
                if hasattr(widget, 'canvas'):
                    widget.canvas.ask_update()
                if hasattr(widget, 'children'):
                    for child in widget.children:
                        update_canvas(child)
            
            update_canvas(self.root)