'''from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
#kivy.require("1.9.1")

class MainPage(GridLayout):
	def __init__(self, **kwargs):
		super(MainPage, self).__init__(**kwargs)
		
		self.cols = 2
		
		self.username = TextInput(multiline=False)
		self.add_widget(self.username)
		self.add_widget(Label(text = "Welcome to our algorithms prog!"))

class FirstKivyApp(App):
	def build(self):
		return MainPage()

if __name__ == "__main__":
	FirstKivyApp().run()'''

from kivy.app import App
from kivy.lang import Builder
#from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from Algorithms import euler_func
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView


class MainMenu(Screen):
	def __init__(self, **kwargs):
		super(MainMenu, self).__init__(**kwargs)
		self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		# Make sure the height is such that there is something to scroll.
		self.layout.bind(minimum_height=self.layout.setter('height'))
		for i in range(20):
			self.btn = Button(text=str(i), size_hint_y=None, height=40)
			self.layout.add_widget(self.btn)
		self.root = ScrollView(size_hint=(None, None), size=(400, 500), pos_hint={"right":0.75, "top":1})
		self.root.add_widget(self.layout)
		self.add_widget(self.root)
		
class EulerFunction(Screen):
	def __init__(self, **kwargs):
		super(EulerFunction, self).__init__(**kwargs)
		self.btn1 = Button(text="Input", size_hint=(0.3, 0.2), pos_hint={"right":1, "top":1})
		self.btn1.bind(on_press=self.buttonClicked)
		self.add_widget(self.btn1)
		self.lbl1 = Label(text="test", size_hint=(0.3, 0.2), pos_hint={"right":1, "bottom":1})
		self.add_widget(self.lbl1)
		self.txt1 = TextInput(multiline=False, size_hint=(0.3, 0.2))
		self.add_widget(self.txt1)
	
	def buttonClicked(self, btn):
		result = euler_func(int(self.txt1.text))
		self.lbl1.text = "The answer is " + str(result)
	
class ScreenManagement(ScreenManager):
	pass
	
presentation = Builder.load_file("Algorithm.kv")

class AlgorithmApp(App):
	def build(self):
		return presentation
		
if __name__ == "__main__":
	AlgorithmApp().run()
	
	
	
	
	
	