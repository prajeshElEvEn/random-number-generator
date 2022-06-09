import kivy
kivy.require('1.9.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import random

class RootApp(BoxLayout):
    def __init__(self):
        super(RootApp, self).__init__()

    def generate_number(self):
        self.random_label.text = str(random.randint(1, 1000))

    def clear_number(self):
        self.random_label.text = '-'

class randomNumberApp(App):
    def build(self):
        return RootApp()

ourApp = randomNumberApp()
ourApp.run()
