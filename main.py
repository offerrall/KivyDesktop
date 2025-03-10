from kivy.lang import Builder
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from button import DButton
from kivy.metrics import dp

# Cargar archivos KV
Builder.load_file('styles.kv')

class CustomBox(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        layout = CustomBox()
        layout.background_color = [1, 0, 0, 1]
        layout.orientation = "vertical"
        layout.padding = 10
        layout.spacing = 10
        
        # Botón con valores predeterminados
        btn1 = DButton( 
            release_callback=self.button_callback,
        )
        
        # Botón con colores personalizados
        btn2 = DButton(
            border_line_width=dp(1.5),
            release_callback=self.button_callback
        )
        
        # Botón con formato diferente
        btn3 = DButton(
            border_line_width=dp(2),
            release_callback=self.button_callback
        )
        
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)
        return layout
    
    def button_callback(self, button):
        print(f"Botón presionado: {button}")

if __name__ == "__main__":
    MainApp().run()