#documentation: https://kivy.org/doc/stable/_modules/kivy/config.html
from kivy.config import Config
from kivy.core.window import Window


class My_config():
    #Config.read('myApp.ini`)
    Config.set('input', 'mtdev', 'disable')
    Config.set('input', 'mtdev', 'disable') # Add this line to disable MTDev
    Config.set('kivy','exit_on_escape',1) #esc to exit
    
    #Config.set('graphics','borderless',1) #no resize,no borders #todo add exit button
    #Config.set('graphics','resizable',0)
    Config.set('graphics','borderless',0)
    Config.set('graphics','resizable',1)
    
    Config.write()
    ####
    Window.size = (400, 500) #width, height
    