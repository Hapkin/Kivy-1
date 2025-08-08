### kivy stuff
import kivy
from kivy.app import App
from kivy.config import Config
from kivy.lang import Builder
from kivy.uix.widget import Widget
### python stuff
#import logging
### my stuff
import view.layouts as layout
Config.read('config.ini')
#issue with a automatic load by kivy that provided an Error
#this disables the error from showing
#Logger.manager.getLogger('kivy.input').setLevel(logging.CRITICAL)


# Designate Our .kv design file 
Builder.load_file('view/main.kv')

class MyLayout(Widget):
	pass

class MyApp(App):
    def build(self):
        self.title = "my_app_title"
        #kv_directory ='view'
        #return layout.MainWindow()
        return MyLayout()


app = MyApp()
app.run()