from kivy.app import App
from kivy.uix.widget import Widget
# from kivy.graphics import Color, Ellipse, Line
# from kivy.uix.image import Image
from kivy.uix.label import Label
# from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.uix.floatlayout import FloatLayout

Builder.load_string("""
<Button>:
    font_size: root.width/5

<FloatLayout>:
    Button:
        text: "hello world"
        size_hint: .2, .1
        pos_hint:{"right":.5,"top":.3}
        color: 0, 1, 0, 1
        

    Button:
        text: "k world"
        size_hint: .2, .1
        pos_hint:{"right":.7,"top":.3}
        color: 0, 1, 0, 1

""")

# class loginscreen(Widget):
#     pass

class MyPaintApp(App):
    def build(self):
        return FloatLayout()


if __name__ == '__main__':
    MyPaintApp().run()