import kivy

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup

class CustomPopup(Popup):
    pass

class SampleBoxLayout(BoxLayout):

    check_box_active = ObjectProperty()

    def checkbox_18_clicked(self, instance, value):
        if value is True:
            print("Checkbox checked")

        else:
            print("Checkbox is Unchecked")

    blue = ObjectProperty()
    red = ObjectProperty()
    green = ObjectProperty()

class SampleApp(App):
    def build(self):
        Window.clearcolor = (0, 0, 0, 1)
        return SampleBoxLayout()

sample_app = SampleApp()
sample_app.run()