
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from Algorithms import *


class MainMenu(Screen):
	pass
	'''def __init__(self, **kwargs):
		super(MainMenu, self).__init__(**kwargs)
		self.layout_content.bind(minimum_height=self.layout_content.setter('height'))	
		
		self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
		
		# Make sure the height is such that there is something to scroll.
		self.layout.bind(minimum_height=self.layout.setter('height'))
		
		all_funcs_list = ["Prime checker", "Factorization", "Euler function", "Mebuis function", 
		"Generator checker", "Search generator", "Modular inversion", "Linear congruence", 
		"System of linear congruencies", "Legendre symbol", "Tonelli-Shanks method", 
		"Sum of two points of elliptic curve", "Point order", "Shift register", 
		"Silver-Pohlig-Hellman algorithm"]
		
		for func in all_funcs_list:
			self.btn = Button(text=func, size_hint_y=None, height=40)
			self.btn.bind(on_press = self.change_screen(func[0]))
			self.layout.add_widget(self.btn)
		
		self.root = ScrollView(size_hint=(None, None), size=(400, 500), pos_hint={"right":0.75, "top":1})
		self.root.add_widget(self.layout)
		self.add_widget(self.root)
	
	def change_screen(self, name):
		sm.current = name.lower()'''

class PrimeChecker(Screen):
	def __init__(self, **kwargs):
		super(PrimeChecker, self).__init__(**kwargs)
		
		self.tip = Label(text="Write the number you want to check:", size_hint=(0.2, 0.1), 
		pos_hint={"right":0.2, "top":1}, font_size=0.14*self.height)
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.9},
		font_size=0.2*self.height)
		self.add_widget(self.data)
		
		self.btn = Button(text="Check!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.9})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.3, "top":0.6})
		self.add_widget(self.answ)
		
	def action(self, btn):
		answer = is_prime(int(self.data.text))
		self.answ.text = str(answer)

		
class Factorization(Screen):
	def __init__(self, **kwargs):
		super(Factorization, self).__init__(**kwargs)
		
		self.tip = Label(text="Write the number you want to factorize:", size_hint=(0.2, 0.1), 
		pos_hint={"right":0.2, "top":1}, font_size=0.14*self.height)
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.9},
		font_size=0.2*self.height)
		self.add_widget(self.data)
		
		self.btn = Button(text="Factorize!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.9})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.3, "top":0.6})
		self.add_widget(self.answ)
		
	def action(self, btn):
		answer = factorize(int(self.data.text))
		for num in answer:
			answer[answer.index(num)]=str(num)
		self.answ.text = self.data.text+" = "+"*".join(answer)

		
class EulerFunction(Screen):
	def __init__(self, **kwargs):
		super(EulerFunction, self).__init__(**kwargs)
		
		self.btn1 = Button(text="Calculate!", size_hint=(0.3, 0.2), pos_hint={"left":1, "bottom":1})
		self.btn1.bind(on_press=self.buttonClicked)
		self.add_widget(self.btn1)
		
		self.lbl1 = Label(text="test", size_hint=(0.3, 0.2), pos_hint={"right":1, "top":1})
		self.add_widget(self.lbl1)
		
		self.txt1 = TextInput(multiline=False, size_hint=(0.3, 0.2), pos_hint={"left":1, "top":1})
		self.add_widget(self.txt1)
	
	def buttonClicked(self, btn):
		result = euler_func(int(self.txt1.text))
		self.lbl1.text = "The answer is " + str(result)


class MebuisFunction(Screen):
	def __init__(self, **kwargs):
		super(MebuisFunction, self).__init__(**kwargs)
		
		
class GeneratorChecker(Screen):
	def __init__(self, **kwargs):
		super(GeneratorChecker, self).__init__(**kwargs)

		
class SearchGenerator(Screen):
	def __init__(self, **kwargs):
		super(SearchGenerator, self).__init__(**kwargs)

		
class ModularInversion(Screen):
	def __init__(self, **kwargs):
		super(ModularInversion, self).__init__(**kwargs)
	
	
class LinearCongruence(Screen):
	def __init__(self, **kwargs):
		super(LinearCongruence, self).__init__(**kwargs)


class SystemOfLinearCongruencies(Screen):
	def __init__(self, **kwargs):
		super(SystemOfLinearCongruencies, self).__init__(**kwargs)

		
class LegendreSymbol(Screen):
	def __init__(self, **kwargs):
		super(LegendreSymbol, self).__init__(**kwargs)

		
class TonelliShanksMethod(Screen):
	def __init__(self, **kwargs):
		super(TonelliShanksMethod, self).__init__(**kwargs)
		

class SumOfTwoPoints(Screen):
	def __init__(self, **kwargs):
		super(SumOfTwoPoints, self).__init__(**kwargs)
		
		

		
class ScreenManagement(ScreenManager):
	pass

	
presentation = Builder.load_file("Algorithm.kv")


class AlgorithmApp(App):
	def build(self):
		return presentation
		
if __name__ == "__main__":
	AlgorithmApp().run()
	
	
	
	
	
	