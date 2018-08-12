from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.core.audio import SoundLoader
from kivy.graphics import *
from kivy.uix.button import Button
import smtplib
import random
from kivy.uix.textinput import TextInput
import pickle
# #server.ehlo()
#server.sendmail("notabot69.py@gmail.com", "8654051718@sms.myboostmobile.com", var)

#txt.att.net sms.myboostmobile.com
#"messaging.sprintpcs.com",  "vmobl.com"
class Menu(Widget):
    def __init__(self):
        super(Menu, self).__init__()
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login("resatikul@gmail.com", "Islam2002@")
        self.emailExtensions = ["sms.myboostmobile.com", "txt.att.net", "mms.cricketwireless.net", "tmomail.net", "email.uscc.net", "vtext.com",]
        self.send = Button(center_x=Window.width/4*3, center_y = Window.height/4,
                           text="Send Message", width = Window.width/4, height = Window.height/4)
        self.number = TextInput(text='', x=Window.width/4, y=Window.height/4*3, width = Window.width/3,height = Window.height/12 , multiline=False)
        self.message = TextInput(text='', x=Window.width/4, y=Window.height/4*2, width = Window.width/2)
        self.send.bind(on_press=self.sendText)
        self.messageLabel = Label(text="enter message here", x=Window.width/4, y=Window.height/4*2.5)
        self.numberLabel = Label(text="enter number/address here", x=Window.width/4, y=Window.height/4*3.2)
        self.sentLabel = Label(text="", x=Window.width/4, y=Window.height/6)
        self.add_widget(self.send)
        self.add_widget(self.number)
        self.add_widget(self.message)
        self.add_widget(self.messageLabel)
        self.add_widget(self.numberLabel)
        self.add_widget(self.sentLabel)

        self.extensionLabel = Label(text="being sent to phone", x=Window.width/4, y=Window.height/4*1.5)
        self.add_widget(self.extensionLabel)

        self.phone = Button(center_x=Window.width/8, center_y = Window.height/8,
                           text="use phone number", width = Window.width/8, height = Window.height/8)
        self.phone.bind(on_press=self.changeToPhone)
        self.add_widget(self.phone)

        self.gmail = Button(center_x=Window.width/8, center_y = Window.height/8*2,
                           text="use gmail", width = Window.width/8, height = Window.height/8)
        self.gmail.bind(on_press=self.changeToGmail)
        self.add_widget(self.gmail)

    def sendText(self, *args):
        if self.number.text != "" and self.message.text != "":
            self.sentLabel.text = ""
            for x in range(0, len(self.emailExtensions)):
                self.server.sendmail("notabot69.py@gmail.com", self.number.text+"@"+self.emailExtensions[x], self.message.text)
            self.number.text = ""
            self.message.text = ""
            self.sentLabel.text = "Message sent"
    def changeToPhone(self, *args):
        self.extensionLabel.text = "being sent to phone"
        self.emailExtensions = ["sms.myboostmobile.com", "txt.att.net", "mms.cricketwireless.net", "tmomail.net", "email.uscc.net", "vtext.com",]
    def changeToGmail(self, *args):
        self.extensionLabel.text = "being sent to gmail"
        self.emailExtensions = ["gmail.com"]



class TextApp(App):
    def build(self):
        # game = Game()
        # return game
        top = Widget()
        top.add_widget(Menu())
        return top

if __name__ == '__main__':
    TextApp().run()