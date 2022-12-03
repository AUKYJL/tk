import random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
import random


class LabWidget(BoxLayout):
    def clicker(self,instance):
        print(instance.text + ' was clicked ' + instance.state)
    def change_bg_color(self,btn:Button):
        colors = ['red','blue','yellow']
        btn.background_color = random.choice(colors)

    def change_color(self, btn: Button):
        colors = ['red', 'blue', 'yellow']
        btn.color = random.choice(colors)
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        b1 = Button(text='Button1')
        b2 = Button(text='Button2')
        b3 = Button(text='Button3',)
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
        for btn in [b1,b2,b3]:
            btn.bind(on_press=self.change_bg_color)
        box_layout = BoxLayout(orientation='vertical')

        b_b1 = Button(text='Button B1')
        b_b2 = Button(text='Button B2')
        b_b3 = Button(text='Button B3')
        for btn in [b_b1,b_b2,b_b3]:
            btn.bind(on_press=self.change_color)
        b_b1.bind(on_press=self.clicker)
        b_b2.bind(on_press=self.clicker)
        b_b3.bind(on_press=self.clicker)
        box_layout.add_widget(b_b1)
        box_layout.add_widget(b_b2)
        box_layout.add_widget(b_b3)
        self.add_widget(box_layout)



class MyApp(App):
    def build(self):
        return LabWidget()


if __name__ == '__main__':
    MyApp().run()
