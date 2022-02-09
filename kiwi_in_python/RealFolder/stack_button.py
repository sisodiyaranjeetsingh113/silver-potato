import kivy     
kivy.require("1.9.1")      
from kivy.app import App     
from kivy.uix.button import Button    
from kivy.uix.stacklayout import StackLayout   
  
class StackLayout_Demo(App):    
          
    def build(self):   
             
        SL = StackLayout(orientation ='bt-rl') # Different orientation ['lr-tb', 'tb-lr', 'rl-tb', 'tb-rl', 'lr-bt', 'bt-lr', 'rl-bt', 'bt-rl']  
        button1 = Button(text ="1",   
                      font_size = 18,   
                      size_hint =(.1, .1))   
        button2 = Button(text ="2",   
                      font_size = 18,   
                      size_hint =(.1, .1))   
        button3 = Button(text ="3",   
                      font_size = 18,   
                      size_hint =(.1, .1))   
        button4 = Button(text ="4",   
                      font_size = 18,   
                      size_hint =(.1, .1))   
        button5 = Button(text ="5",   
                      font_size = 18,   
                      size_hint =(.1, .1))   
        button6 = Button(text ="6",   
                    font_size = 18,   
                    size_hint =(.1, .1))   
        button7 = Button(text ="7",   
                    font_size = 18,   
                    size_hint =(.1, .1))   
        button8 = Button(text ="8",   
                    font_size = 18,   
                    size_hint =(.1, .1))   
        button9 = Button(text ="9",   
                    font_size = 18,   
                    size_hint =(.1, .1))   
        button0 = Button(text ="0",   
                    font_size = 18,   
                    size_hint =(.1, .1))   
          
        button11 = Button(text ="11",   
                    font_size = 18,   
                    size_hint =(.1, .1))  
        # adding widgets   
        SL.add_widget(button1)   
        SL.add_widget(button2)   
        SL.add_widget(button3)   
        SL.add_widget(button4)   
        SL.add_widget(button5)   
        SL.add_widget(button6)   
        SL.add_widget(button7)   
        SL.add_widget(button8)   
        SL.add_widget(button9)   
        SL.add_widget(button0)   
      
        return SL   
root = StackLayout_Demo()  
root.run()           