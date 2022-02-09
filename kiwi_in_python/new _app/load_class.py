import abc
from abc import ABC, ABCMeta
from typing import Union, Any
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.layout import Layout
from kivy.uix.button import Button

class MyNewApp(Layout):
    def __init__(self, **agrs):
        super(MyNewApp, self).__init__()
        self.oprerand1_label = Label(text="Operand1:", pos=[20, 600], size=[100, 30])
        self.add_widget(self.oprerand1_label)
        self.operand1_input_field = TextInput(multiline=False, pos=[200, 600], size=[100, 30])
        self.add_widget(self.operand1_input_field)
        self.oprerand2_label = Label(text="Operand2:", pos=[20, 550], size=[100, 30])
        self.add_widget(self.oprerand2_label)
        self.operand2_input_field = TextInput(multiline=False, pos=[200, 550], size=[100, 30])
        self.add_widget(self.operand2_input_field)
        self.Answer_label = Label(text="Answer is:", pos=[20, 500], size=[100, 30])
        self.add_widget(self.Answer_label)
        self.answer_input_field = TextInput(multiline=False, pos=[200, 500], size=[100, 30])
        self.add_widget(self.answer_input_field)
        self.press = Button(text="Click me..", pos=[120, 450], size=[80, 30])
        self.press.bind(on_press=self.click_me)
        self.add_widget(self.press)
    def click_me(self, obj):
        if (self.operand1_input_field.text):
            x = int(self.operand1_input_field.text)
        else:
            x=0
        if (self.operand2_input_field.text):
            y = int(self.operand2_input_field.text)
        else:
            y=0
        self.answer_input_field.text = str(x + y)
        self.operand1_input_field.text = ""
        self.operand2_input_field.text = ""
class MyActualApp(App):
    def build(self):
        return MyNewApp()
if __name__ == "__main__":
    MyActualApp().run()
