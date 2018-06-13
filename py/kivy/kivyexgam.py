from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.graphics import Color, Ellipse, Line
# from kivy.uix.image import Image
# from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.lang.builder import Builder
# from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.widget import Widget
from kivy.graphics import Line

class Painter(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            self.line = Line(points=(touch.x, touch.y))
    
    def on_touch_move(self, touch):
        self.line.points += [touch.x, touch.y]

class MainScreen(Screen):
    pass

class GameScreen(Screen):
    pass

class ScreenManagement(ScreenManager):
    pass

Presentation = Builder.load_string("""
#: import FadeTransition kivy.uix.screenmanager.FadeTransition


ScreenManagement:
    transition: FadeTransition()
    MainScreen:
    GameScreen:


<Button>:
    font_size: ((root.width/3)+(root.height/3))/2


<MainScreen>:
    name:"main"

    FloatLayout:
        Button:
            size_hint: .3,.1
            on_release: app.root.current = "game"
            text: "Start"
            color: 1, 1, 0, 1
            background_color: 0, 0, .5, 1
            border: 15,16,16,10
            pos_hint:{"right":.7,"top":.5}
 
<GameScreen>:
    name:"game"
    FloatLayout:
        Painter:
            id: painter
        Button:
            color: 0,1,0,1
            size_hint: .2,.1
            text:'quit'
            on_release: app.root.current = "main"
            on_release: painter.canvas.clear()
            pos_hint: {"right":1,"top":1}

""")




class MyPaintApp(App):
    def build(self):
        return Presentation


if __name__ == '__main__':
    MyPaintApp().run()