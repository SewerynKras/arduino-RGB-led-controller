import serial
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

ARDUINO_PORT = 'com3'


class Controller(Widget):
    rgb = ListProperty([0, 0, 0])

    def __init__(self):
        super(Controller, self).__init__()

        # open serial communication with arduino
        self.data = serial.Serial(ARDUINO_PORT, 9600)

    def change_color(self, color, value):

        new_color = f"{color}{str(int(value)).zfill(3)}"
        colors = {'r': 0, 'g': 1, 'b': 2}
        self.rgb[colors[color]] = value / 255.0

        self.data.write(new_color.encode())


class controllerApp(App):

    def build(self):
        layout = BoxLayout()
        ctrl = Controller()
        layout.add_widget(ctrl)
        return layout


if __name__ == '__main__':
    controllerApp().run()
