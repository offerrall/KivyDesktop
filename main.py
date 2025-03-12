from kivy.metrics import dp
from kivy_desktop.button import DButton
from kivy_desktop.int import DInt
from kivy_desktop.scroll import DScrollView
from kivy_desktop.app import DApp



scroll_view = DScrollView()

for i in range(4):

    btn = DButton(text=f"Botón {i}",
                  size_hint_y=None,
                  height=dp(50),
                  release_callback=lambda instance: print(instance.text)
                  )
    
    int_input = DInt(size_hint_y=None, height=dp(50), min_value=-10, max_value=10, value=5)
    int_input.bind(value=lambda instance, value: print(value))

    scroll_view.add_widget(int_input)
    scroll_view.add_widget(btn)

app = DApp(main_container=scroll_view, fps=144, title="Kivy Desktop Test")

if __name__ == "__main__":
    app.run()