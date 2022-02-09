import abc
from abc import ABC, ABCMeta
from typing import Union, Any

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.button import Button


@abc.abstractmethod
def click_me(x, y):
    pass


class MyNewApp(Layout):
    def __init__(self, **agrs):
        super(MyNewApp, self).__init__()
        self.Answer_label = Label(text="Answer is:", pos=[20, 500], size=[100, 30])
        self.add_widget(self.Answer_label)
        self.answer_input_field = TextInput(is_focusable=True, multiline=False, pos=[200, 500], size=[100, 30])
        self.add_widget(self.answer_input_field)
        self.press = Button(text="Click me..", pos=[120, 450], size=[80, 30])
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
        self.press.background_color = (1, 0, 0, 1)
    def click_me(self, obj):
        x = ''
        y = ''
        sign1 = self.answer_input_field.text.find('-')
        sign2 = self.answer_input_field.text.find('+')
        sign3 = self.answer_input_field.text.find('*')
        sign4 = self.answer_input_field.text.find('/')

        if sign1 != -1:
            w = self.answer_input_field.text
            z = len(self.answer_input_field.text)
            x = int(w[0:sign1])
            y = int(w[sign1+1:z])
            self.answer_input_field.text = str(x - y)
        if sign2 != -1:
            w = self.answer_input_field.text
            z = len(self.answer_input_field.text)
            x = int(w[0:sign2])
            y = int(w[sign2 + 1:z])
            self.answer_input_field.text = str(x + y)

        if sign3 != -1:
            w = self.answer_input_field.text
            z = len(self.answer_input_field.text)
            x = int(w[0:sign3])
            y = int(w[sign3 + 1:z])

            self.answer_input_field.text = str(x * y)
        if sign4 != -1:
            w = self.answer_input_field.text
            z = len(self.answer_input_field.text)
            x = int(w[0:sign4])
            y = int(w[sign4 + 1:z])
            self.answer_input_field.text = str(x // y)


class MyRealApp(App):
    def build(self):
        return MyNewApp()


if __name__ == "__main__":
    MyRealApp().run()
