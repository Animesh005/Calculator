import kivy
kivy.require("1.10.0")

from kivy.app import App
from kivy.uix.widget import Widget

class CustomWidget(Widget):
    pass

class CustomWidgetApp(App):

    def build(self):
        return CustomWidget()

custWidget = CustomWidgetApp()

custWidget.run()



