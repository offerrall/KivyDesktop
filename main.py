from kivy.metrics import dp
from kivy_desktop.button import DButton
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp

# Función para manejar eventos de botones
def button_callback(button):
    print(f"Botón presionado: {button.text}")

# Función para agregar botones al contenedor
def add_buttons(container):
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
                release_callback=button_callback
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
                release_callback=button_callback
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
                release_callback=button_callback
            )
        elif i % 2 == 0:
            # Botón con contenido alineado a la derecha
            btn = DButton(
                text=f"Botón {i}",
                content_alignment="right",
                size_hint_y=None,
                height=dp(50),
                release_callback=button_callback
            )
        else:
            # Botón con contenido alineado a la izquierda
            btn = DButton(
                text=f"Botón {i}",
                content_alignment="left",
                size_hint_y=None,
                height=dp(50),
                release_callback=button_callback
            )
        
        # Agregar el botón al contenedor
        container.add_widget(btn)

# Crear un DScrollView como contenedor principal
scroll_view = DScrollView()

# Agregar botones al scroll view
add_buttons(scroll_view)

# Crear y ejecutar la aplicación con el scroll_view como contenedor
app = DApp(container=scroll_view)

if __name__ == "__main__":
    app.run()