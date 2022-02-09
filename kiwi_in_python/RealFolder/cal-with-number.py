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
        self.answer_input_field = TextInput(text='', is_focusable=True, multiline=False, pos=[20, 500], size=[160, 30])
        self.add_widget(self.answer_input_field)
        self.press = Button(text ="=", font_size = 18, size_hint =(.1, .1),pos= [180, 380], size=[80, 30])
        self.press.bind(on_press=self.click_me)
        self.button1 = Button(text ="1", font_size = 18, size_hint =(.1, .1), pos= [20, 470], size=[80, 30])   
        self.button2 = Button(text ="2", font_size = 18, size_hint =(.1, .1), pos= [100, 470], size=[80, 30])   
        self.button3 = Button(text ="3",font_size = 18,size_hint =(.1, .1), pos= [180, 470], size=[80, 30])             
        self.button4 = Button(text ="4",font_size = 18,size_hint =(.1, .1), pos= [20, 440], size=[80, 30])      
                      
        self.button5 = Button(text ="5",font_size = 18,size_hint =(.1, .1), pos= [100, 440], size=[80, 30])   
                      
        self.button6 = Button(text ="6",font_size = 18,size_hint =(.1, .1), pos= [180, 440], size=[80, 30])      
        self.button7 = Button(text ="7",font_size = 18,size_hint =(.1, .1), pos= [20, 410], size=[80, 30])
        self.button8 = Button(text ="8",font_size = 18,size_hint =(.1, .1), pos= [100, 410], size=[80, 30])      
        self.button9 = Button(text ="9",font_size = 18,size_hint =(.1, .1), pos= [180, 410], size=[80, 30])      
        self.button0 = Button(text ="0",font_size = 18,size_hint =(.1, .1), pos= [100, 380], size=[80, 30])  
        self.button00 = Button(text ="00",font_size = 18,size_hint =(.1, .1), pos= [20, 380], size=[80, 30])      
        self.button_clear = Button(text ="C",font_size = 18,size_hint =(.1, .1), pos= [180, 500], size=[80, 30])      
        self.button_clearAll = Button(text ="CA",font_size = 18,size_hint =(.1, .1), pos= [260, 500], size=[80, 30])      
        
        self.button_add = Button(text ="+",font_size = 18,size_hint =(.1, .1), pos= [260, 470], size=[80, 30])      
        self.button_sub = Button(text ="-",font_size = 18,size_hint =(.1, .1), pos= [260, 440], size=[80, 30])  
        self.button_multi = Button(text ="*",font_size = 18,size_hint =(.1, .1), pos= [260,410], size=[80, 30])      
        self.button_div = Button(text ="/",font_size = 18,size_hint =(.1, .1), pos= [260, 380], size=[80, 30])      
        self.button0.bind(on_press=self.click_me)
        self.button00.bind(on_press=self.click_me)
        self.button1.bind(on_press=self.click_me)
        self.button2.bind(on_press=self.click_me)
        self.button3.bind(on_press=self.click_me)
        self.button4.bind(on_press=self.click_me)
        self.button5.bind(on_press=self.click_me)
        self.button6.bind(on_press=self.click_me)
        self.button7.bind(on_press=self.click_me)
        self.button8.bind(on_press=self.click_me)
        self.button9.bind(on_press=self.click_me)
        self.button_add.bind(on_press=self.click_me)
        self.button_sub.bind(on_press=self.click_me)
        self.button_multi.bind(on_press=self.click_me)
        self.button_div.bind(on_press=self.click_me)
        self.button_clearAll.bind(on_press=self.click_me)
        self.button_clear.bind(on_press=self.click_me)
        # adding widgets   
        self.add_widget(self.button1)   
        self.add_widget(self.button2)   
        self.add_widget(self.button3)   
        self.add_widget(self.button4)   
        self.add_widget(self.button5)   
        self.add_widget(self.button6)   
        self.add_widget(self.button7)   
        self.add_widget(self.button8)   
        self.add_widget(self.button9)   
        self.add_widget(self.button0)  
        self.add_widget(self.button00)
        self.add_widget(self.button_clear)  
        self.add_widget(self.button_clearAll)
        self.add_widget(self.button_add)
        self.add_widget(self.button_sub)
        self.add_widget(self.button_multi)
        self.add_widget(self.button_div)
        
        self.add_widget(self.press)
        self.button_clear.background_color = (1, 0, 0, 1)
        self.button_clearAll.background_color = (1, 0, 0, 1)
        self.press.background_color = (1, 0, 0, 1)
        self.button_add.background_color = (1, 0, 0, 1)
        self.button_sub.background_color = (1, 0, 0, 1)
        self.button_multi.background_color = (1, 0, 0, 1)
        self.button_div.background_color = (1, 0, 0, 1)
    def click_me(self, obj):
        if obj.text == '=':    
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
        elif obj.text == '1': self.answer_input_field.text=self.answer_input_field.text+'1'
        elif obj.text == '2': self.answer_input_field.text=self.answer_input_field.text+'2'
        elif obj.text == '3': self.answer_input_field.text=self.answer_input_field.text+'3'
        elif obj.text == '4': self.answer_input_field.text=self.answer_input_field.text+'4'
        elif obj.text == '5': self.answer_input_field.text=self.answer_input_field.text+'5'
        elif obj.text == '6': self.answer_input_field.text=self.answer_input_field.text+'6'
        elif obj.text == '7': self.answer_input_field.text=self.answer_input_field.text+'7'
        elif obj.text == '8': self.answer_input_field.text=self.answer_input_field.text+'8'
        elif obj.text == '9': self.answer_input_field.text=self.answer_input_field.text+'9'
        elif obj.text == '0': self.answer_input_field.text=self.answer_input_field.text+'0'
        elif obj.text == '00': self.answer_input_field.text=self.answer_input_field.text+'00'
        elif obj.text == '+': self.answer_input_field.text=self.answer_input_field.text+'+'
        elif obj.text == '-': self.answer_input_field.text=self.answer_input_field.text+'-'
        elif obj.text == '*': self.answer_input_field.text=self.answer_input_field.text+'*'
        elif obj.text == '/': self.answer_input_field.text=self.answer_input_field.text+'/'
        elif obj.text == 'CA': self.answer_input_field.text=''
        elif obj.text == 'C': 
            self.answer_input_field.text=self.answer_input_field.text[0:len(self.answer_input_field.text)-1]
                

class MyRealApp(App):
    def build(self):
        return MyNewApp()


if __name__ == "__main__":
    MyRealApp().run()
 