from kivy.metrics import dp
from kivy.graphics import Color, Rectangle
from kivy_desktop.button import DButton
from kivy_desktop.int import DInt
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class BackgroundWidget(BoxLayout):
    def __init__(self, **kwargs):
        super(BackgroundWidget, self).__init__(**kwargs)
        with self.canvas.before:
            Color(0.25, 0.25, 0.25, 1)  # Rojo (R=1, G=0, B=0, A=1)
            self.rect = Rectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self._update_rect, size=self._update_rect)
    
    def _update_rect(self, instance, value):
        self.rect.pos = self.pos
        self.rect.size = self.size


# Creamos un contenedor que tiene un fondo rojo y ocupa toda la ventana
background = BackgroundWidget(orientation='vertical')

# Creamos el ScrollView que irá dentro del contenedor con fondo rojo
# Usamos size_hint=(1, 1) para que ocupe todo el espacio disponible
scroll_view = DScrollView(size_hint=(1, 1))

# Ajustamos el padding y spacing para que los widgets estén más separados
scroll_view.layout.padding = [dp(20), dp(20), dp(20), dp(20)]  # [left, top, right, bottom]
# Creamos widgets más grandes
for i in range(10):
    if i < 2:
        continue
    
    # Aumentamos el tamaño de los widgets
    HEIGHT = dp(i * 15)  # Multiplicamos por 15 en lugar de 10 para hacerlos más altos
    print(HEIGHT)
    
    # Botón con texto más grande y que ocupe el ancho completo
    btn = DButton(
        text=f"Height: {HEIGHT}",
        size_hint_y=None,
        size_hint_x=1,  # Ocupa todo el ancho disponible
        height=HEIGHT,
        release_callback=lambda instance: print(instance.text)
    )
    
    # Widget de entrada de enteros con tamaño más grande
    int_input = DInt(
        size_hint_y=None,
        size_hint_x=1,  # Ocupa todo el ancho disponible
        height=HEIGHT,
        min_value=-10,
        max_value=10,
        value=5,
        border_line_width=dp(1.2),
    )
    
    int_input.bind(value=lambda instance, value: print(value))

    scroll_view.add_widget(btn)
    scroll_view.add_widget(int_input)

# Añadimos el ScrollView al widget de fondo
background.add_widget(scroll_view)

# Usamos el widget de fondo como contenedor principal
app = DApp(main_container=background, fps=144, title="Kivy Desktop Test")

if __name__ == "__main__":
    app.run()