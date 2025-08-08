##
## testing handler
##

from kivy.uix.button import Button

def handle_button_clicked(self):
    self.counter+=1
    self.background_color=("#19613A")
    self.text = f"Hello, World! {self.counter} clicked"
