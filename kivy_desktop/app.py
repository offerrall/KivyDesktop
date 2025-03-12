from kivy.app import App
from kivy.config import Config

class DApp(App):

    def __init__(self, container, **kwargs):
        Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
        self.container = container
        super(DApp, self).__init__(**kwargs)

    def build(self):
        return self.container 