from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
import random
from kivy.uix.camera import Camera

Titile = str(random.random())

class Game(Widget):
    def __init__(self, *a, **k):
        super().__init__(**k)
        self.button = Button(text='Hello world', font_size=14)
        self.add_widget(self.button)
        self.cam = Camera(play=True)
        self.add_widget(self.cam)

class TApp(App):
    def build(self):
        self.title = Titile
        wdg = Widget()
        wdg.add_widget(Game())
        return wdg

tt = TApp()
tt.run()