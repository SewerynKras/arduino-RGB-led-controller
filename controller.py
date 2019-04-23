import serial
import os
# disable kivy argument parser since it's not needed
os.environ["KIVY_NO_ARGS"] = "1"
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
import argparse
import struct


class Controller(Widget):
    rgb = ListProperty([0, 0, 0])

    def __init__(self, port):
        super(Controller, self).__init__()

        # open serial communication with Arduino
        self.data = serial.Serial(port=port, baudrate=9600)

    def change_color(self, color, value):
        """
        This function gets called every time the user
        changes any of the sliders

        Arguments:
            color {str} -- either "red", "green" or "blue"
            value {float} -- value between 0.0 and 255.0
        """

        color_map = {'red': 0, 'green': 1, 'blue': 2}
        self.rgb[color_map[color]] = value / 255.0

        # Arduino is set up to receive 2 bytes of data:
        # 0: color code -- either 0, 1 or 2 as described in color_map
        # 1: color value -- int between 0 and 255
        message = struct.pack("BB", color_map[color], int(value))
        self.data.write(message)


class controllerApp(App):

    def __init__(self, port):
        super(controllerApp, self).__init__()
        self.port = port

    def build(self):
        layout = BoxLayout()
        controller = Controller(port=self.port)
        layout.add_widget(controller)
        return layout


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Control an arduino RGB strip over serial port')
    parser.add_argument('port', help='Serial port that Arduino is connected to')
    args = parser.parse_args()
    controllerApp(port=args.port).run()
