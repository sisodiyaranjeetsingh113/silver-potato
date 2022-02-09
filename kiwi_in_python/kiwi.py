import kivy
from kivy.app import App
from kivy.uix.label import Label
import kivy.uix.textinput
class MyApp(App):
    def build(self):
        return Label(text='This is MyApp')
if __name__ == "__main__" :
    MyApp().run()
