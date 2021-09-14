# kivy clacl app version 0.2

from math import sqrt as sq

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.label import Label

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class MyApp(App):


    def build(self):
        self.formul = ""
        bl  = BoxLayout(orientation='vertical', padding=25)
        gl = GridLayout(cols=5, spacing=3, size_hint=(1,.6))
        
        self.labl = Label(text='0',font_size = 40, halign='right', valign='center', size_hint=(1,.4), text_size=(Window.size[0]-50, Window.size[1]*.4-50))
        bl.add_widget(self.labl)

        gl.add_widget(Button(text='7', on_press=self.addnumber_op))
        gl.add_widget(Button(text='8', on_press=self.addnumber_op))
        gl.add_widget(Button(text='9', on_press=self.addnumber_op))
        gl.add_widget(Button(text='ce', on_press=self.clearformul))
        gl.add_widget(Button(text='<-', on_press=self.clearformul))
        

        gl.add_widget(Button(text='4', on_press=self.addnumber_op))
        gl.add_widget(Button(text='5', on_press=self.addnumber_op))
        gl.add_widget(Button(text='6', on_press=self.addnumber_op))
        gl.add_widget(Button(text='x', on_press=self.addnumber_op))
        gl.add_widget(Button(text='/', on_press=self.addnumber_op))

        gl.add_widget(Button(text='1', on_press=self.addnumber_op))
        gl.add_widget(Button(text='2', on_press=self.addnumber_op))
        gl.add_widget(Button(text='3', on_press=self.addnumber_op))
        gl.add_widget(Button(text='-', on_press=self.addnumber_op))

        gl.add_widget(Button(text='+', on_press=self.addnumber_op))
        gl.add_widget(Button(text='.', on_press=self.addnumber_op))
        gl.add_widget(Button(text='0', on_press=self.addnumber_op))
        gl.add_widget(Button(text='=', on_press=self.result))
        gl.add_widget(Button(text='√', on_press=self.addnumber_op))
        gl.add_widget(Button(text='^', on_press=self.addnumber_op))
        
        
        bl.add_widget(gl)

        return bl

    def update_lbl(self):
        self.labl.text = self.formul

    def addnumber_op(self, instance):
        if instance.text == "^":
            self.formul += "**"
            self.labl.text += "^"

        elif instance.text == "x":
            self.formul += "*"
            self.labl.text += "x"

        elif instance.text == '√':
            self.formul = sq(float(self.formul))
            self.formul = str(self.formul)
            self.update_lbl()

        else:
            self.formul += str(instance.text)
            self.update_lbl()



    def clearformul(self, instance):
        if instance.text == "<-":
            p  = type(self.formul)
            p = str(p)
            if p != "<class 'str'>":
                self.formul = str(self.formul)
            self.formul = self.formul[:-1]
        else: self.formul = ""
        self.update_lbl()

    def result(self, instance):
        self.labl.text = str(eval(self.formul))
        self.formul = self.labl.text 

    
if __name__ == '__main__':
    MyApp().run()

