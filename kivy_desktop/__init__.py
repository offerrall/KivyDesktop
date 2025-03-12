from kivy.lang import Builder
from pathlib import Path
from kivy.config import Config

Builder.load_file(str(Path(__file__).parent / 'styles.kv'))

 
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'maxfps', '0')
