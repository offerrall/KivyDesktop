from kivy.metrics import dp
from kivy_desktop.button import DButton
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp


def button_callback(button):
    print(f"Botón presionado: {button.text}")

def add_buttons(container):

    for i in range(5):

        btn = DButton(
            text=f"Botón {i}",
            size_hint_y=None,
            height=dp(50),
            release_callback=button_callback
        )

        container.add_widget(btn)


scroll_view = DScrollView()
add_buttons(scroll_view)
app = DApp(main_container=scroll_view)

if __name__ == "__main__":
    app.run()