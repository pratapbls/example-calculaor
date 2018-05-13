import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class calcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text=str(eval(calculation))
            except:
                self.display.text = "Error"
class calculatorApp(App):
    def build(self):
        return calcGridLayout()

calcApp = calculatorApp()
calcApp.run()
print("hello")
