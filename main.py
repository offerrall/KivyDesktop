from kivy.metrics import dp
from kivy_desktop.button import DButton
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp



scroll_view = DScrollView()

for i in range(5):

    btn = DButton(text=f"Botón {i}",
                  size_hint_y=None,
                  height=dp(50),
                  release_callback=lambda instance: print(instance.text)
                  )

    scroll_view.add_widget(btn)

app = DApp(main_container=scroll_view)

if __name__ == "__main__":
    app.run()