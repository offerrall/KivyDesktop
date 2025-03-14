from kivy.lang import Builder
from kivy.config import Config

from pathlib import Path

Builder.load_file(str(Path(__file__).parent / 'styles.kv'))

 
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('graphics', 'maxfps', '0')
