import serial
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget

ARDUINO_PORT = 'com4'


class Controller(Widget):
    rgb = ListProperty([1, 0, 0])

    def __init__(self):
        super(Controller, self).__init__()

        # open serial communication with arduino
        self.data = serial.Serial(ARDUINO_PORT, 9600)

    def send_data(self, *args):

        # join the color channels in a way that each value is 3 digits long
        output = ''.join([str(int(i * 255)).zfill(3) for i in self.rgb])

        # send arduino the 9 digit long string converted to bytes
        self.data.write(output.encode())


class controllerApp(App):

    def build(self):
        layout = BoxLayout()
        ctrl = Controller()
        layout.add_widget(ctrl)
        return layout


if __name__ == '__main__':
    controllerApp().run()
