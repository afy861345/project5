from kivy.app import App
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.lang import Builder

Window.clearcolor=(0,0,0,1)
Window.size=(400,620)
class Myapp6(App):
    def build(self):
        self.title=("Ali")
        pass

runTouchApp(Builder.load_string('''
ActionBar:
    pos_hint:{'top':1}      
    ActionView:
        ActionPrevious:
            title:"ali"  
        ActionButton:
            text:"Home"
        ActionButton:
            text:"Back"  
        ActionGroup:
            color:(0.3,0.6,2,1)                    
            text:"More"
            ActionButton:
                text:"ALI1"                                             
            ActionButton:
                text:"ALI2" 
            ActionButton:
                text:"ALI3"                     
            ActionButton:
                text:"ALI4" 
'''))


      
Myapp6().run()