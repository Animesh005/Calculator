import kivy

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.button import Label

class HellokivyApp(App):

    def build(self):
        return Label()

hk = HellokivyApp()

hk.run()
