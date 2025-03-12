from kivy.app import App
from kivy.metrics import dp
from kivy_desktop.button import DButton
from kivy_desktop.scroll import DScrollView

class DScrollViewApp(App):
    def build(self):
        # Crear un DScrollView con todas las propiedades predeterminadas
        scroll_view = DScrollView()
        
        # Agregar botones directamente al DScrollView
        self.add_buttons(scroll_view)
        
        return scroll_view
    
    def add_buttons(self, container):
        # Agregar varios botones con diferentes estilos
        for i in range(1, 21):  # 20 botones para demostrar el desplazamiento
            # Crear diferentes estilos según el índice
            if i % 5 == 0:
                # Botón rojo con bordes redondeados
                btn = DButton(
                    text=f"Botón {i}",
                    background_color=[0.8, 0.2, 0.2, 1],
                    border_color=[0.7, 0.1, 0.1, 1],
                    background_radius=[dp(15), dp(15), dp(15), dp(15)],
                    size_hint_y=None,
                    height=dp(50),
                    release_callback=self.button_callback
                )
            elif i % 4 == 0:
                # Botón verde con icono a la derecha
                btn = DButton(
                    text=f"Botón {i}",
                    icon_source="test.png",
                    icon_placement="right",
                    background_color=[0.2, 0.8, 0.2, 1],
                    border_color=[0.1, 0.7, 0.1, 1],
                    size_hint_y=None,
                    height=dp(50),
                    release_callback=self.button_callback
                )
            elif i % 3 == 0:
                # Botón azul con icono a la izquierda
                btn = DButton(
                    text=f"Botón {i}",
                    icon_source="test.png",
                    icon_placement="left",
                    background_color=[0.2, 0.4, 0.8, 1],
                    border_color=[0.1, 0.3, 0.7, 1],
                    size_hint_y=None,
                    height=dp(50),
                    release_callback=self.button_callback
                )
            elif i % 2 == 0:
                # Botón con contenido alineado a la derecha
                btn = DButton(
                    text=f"Botón {i}",
                    content_alignment="right",
                    size_hint_y=None,
                    height=dp(50),
                    release_callback=self.button_callback
                )
            else:
                # Botón con contenido alineado a la izquierda
                btn = DButton(
                    text=f"Botón {i}",
                    content_alignment="left",
                    size_hint_y=None,
                    height=dp(50),
                    release_callback=self.button_callback
                )
            
            # Agregar el botón al contenedor
            container.add_widget(btn)
    
    def button_callback(self, button):
        print(f"Botón presionado: {button.text}")

if __name__ == "__main__":
    DScrollViewApp().run()