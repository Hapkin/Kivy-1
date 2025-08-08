### kivy stuff
import kivy
from kivy.app import App
#from kivy.logger import Logger
#from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.widget import Widget
#from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle, Color
### python stuff

#import logging

### my stuff
import handlers.handler_test as h
import classes.gui_items as gui
import view.total as view
import view.layouts as layout


''''
class DemoApp():
   def build(self):
      lo = BoxLayout(orientation = 'vertical')
      self.l1 = Label(text='Enter your name', font_size=20)
      self.t1 = TextInput(font_size = 30)
      self.b1 = Button(text = 'Submit', size_hint = (None, None),pos_hint={'x':.4, 'y':.2}, size = (200,75))
      lo.add_widget(self.l1)
      lo.add_widget(self.t1)
      lo.add_widget(self.b1)
      return lo
'''   

class MainWindow(FloatLayout): #BoxLayout
    def __init__(self):
        super().__init__()
        view


        self.my_layout = FloatLayout()
#            rows=5, col_force_default=True,
#            col_default_width=100,
#            right=True
#        )
#        self.left_grid = FloatLayout(
#            rows=1, col_force_default=True,
#            col_default_width=100
#       )
        self.spacing=(20,0)
        #buttons
        btn_wecome=gui.Knop("Wecome")#,(0.2, 0.1),{'x': 0.1, 'y': 0.8})
        btn_clicker1=gui.Knop("clicker1",(200,100),(0,300))
        btn_clicker2=gui.Knop("clicker2",(200,100),(0,200))
        btn_clicker3=gui.Knop("clicker1",(200,100),(0,100))
        
        #create menu
        '''
        self.add_widget(btn_wecome)
        self.add_widget(btn_clicker1)
        self.add_widget(btn_clicker2)
        self.add_widget(btn_clicker3)
        '''
        self.my_layout.add_widget(btn_wecome)
        #self.right_grid.add_widget(btn_clicker1)
        #self.right_grid.add_widget(btn_clicker2)
        #self.right_grid.add_widget(btn_clicker3)
        #'''
        self.counter=0


        #exit_button = gui.Knop(text="Exit")
        #exit_button.bind(on_release=App.get_running_app().stop)
        #self.add_widget(exit_button)