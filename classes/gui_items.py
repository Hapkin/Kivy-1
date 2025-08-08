### kivy
from kivy.uix.button import Button

### python

### mine
import handlers.handler_test as h

#Button(ButtonBehavior, Label):
#Button(text='Hello world', font_size=14)
class Knop(Button):
    def __init__(self, text , size=(100,100), position={"x": 0,"y": 0}, back_color=None, on_click=None):
        super().__init__()  
        self.text=text
        self.size_hint=size
        self.pos_hint=position
        if (back_color==None):
            self.background_color=("#0B0757")
        else:
            self.background_color=back_color
        if (on_click==None):
            self.bind(on_press=h.handle_button_clicked)
        else:
            self.on_click=on_click
        self.counter=0



    def build(self):
            # use a (r, g, b, a) tuple
            btn = Button(text ="Push Me !",
                    font_size ="20sp",
                    background_color =(1, 1, 1, 1),
                    color =(1, 1, 1, 1), 
                    size =(32, 32),
                    size_hint=(None, None),
                    pos =(300, 250))
            

            return btn



      