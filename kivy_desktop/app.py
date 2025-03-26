from kivy.app import App

class DApp(App):
    """
    main_container: widget \n
    title:
        type: str
        default: 'Kivy Desktop App' \n
    """
    def __init__(self,
                 main_container,
                 title="Kivy Desktop App",
                 **kwargs):

        self.container = main_container
        kwargs['title'] = title
        super(DApp, self).__init__(**kwargs)
        
        self._update_event = None

    def build(self):
        return self.container