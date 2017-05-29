from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from Algorithms import *

#kivy.require("1.9.1")

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
		
		self.tip = Label(text="Write the number you want to check:", size_hint=(0.85, 0.1), 
		pos_hint={"right":0.9,"top":1}, font_size=0.2*self.height, halign="left", valign="middle")
		self.tip.bind(size=self.tip.setter("text_size"))
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.85})
		self.add_widget(self.data)
		
		self.btn = Button(text="Check!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.85})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.3, "top":0.75}, font_size=0.2*self.height)
		self.add_widget(self.answ)
		
	def action(self, btn):
		answer = is_prime(int(self.data.text))
		self.answ.text = str(answer)

		
class Factorization(Screen):
	def __init__(self, **kwargs):
		super(Factorization, self).__init__(**kwargs)
		
		self.tip = Label(text="Write the number you want to factorize:", size_hint=(0.85, 0.1), 
		pos_hint={"right":0.9, "top":1}, font_size=0.2*self.height)
		self.tip.bind(size=self.tip.setter("text_size"))
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.85})
		self.add_widget(self.data)
		
		self.btn = Button(text="Factorize!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.85})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.4, "top":0.75}, font_size=0.18*self.height)
		self.add_widget(self.answ)
		
	def action(self, btn):
		answer = factorize(int(self.data.text))
		for num in answer:
			answer[answer.index(num)]=str(num)
		self.answ.text = self.data.text+" = "+"*".join(answer)

		
class EulerFunction(Screen):
	def __init__(self, **kwargs):
		super(EulerFunction, self).__init__(**kwargs)
		
		self.tip = Label(text="Euler function is a function which calculates the amount of mutually simple numbers with the given number", size_hint=(0.95, 0.1), 
		pos_hint={"right":1, "top":1}, font_size=0.2*self.height, halign="left")
		self.tip.bind(size=self.tip.setter("text_size"))
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.85})
		self.add_widget(self.data)
		
		self.btn = Button(text="Calculate!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.85})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.4, "top":0.75}, font_size=0.18*self.height)
		self.add_widget(self.answ)
	
	def action(self, btn):
		result = euler_func(int(self.data.text))
		self.answ.text = "The answer is " + str(result)


class MebiusFunction(Screen):
	def __init__(self, **kwargs):
		super(MebiusFunction, self).__init__(**kwargs)
		
		self.tip = Label(text="Möbius function is a function which returns:\n 0 if given number can be divided by number in second power \n 1 if it can be divided by even amount of prides\n -1 if it can be divided by odd amount of prides", 
		size_hint=(0.95, 0.2), pos_hint={"right":1, "top":1}, halign="left")
		self.tip.bind(size=self.tip.setter("text_size"))
		self.add_widget(self.tip)
		
		self.data = TextInput(multiline=False, size_hint=(0.2, 0.05), pos_hint={"right":0.3, "top":0.75})
		self.add_widget(self.data)
		
		self.btn = Button(text="Calculate!", size_hint=(0.1, 0.1), pos_hint={"right":0.5, "top":0.75})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.4, "top":0.65}, font_size=0.18*self.height)
		self.add_widget(self.answ)
	
	def action(self, btn):
		result = mebius_func(int(self.data.text))
		self.answ.text = "The answer is " + str(result)
		
		
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
		

class SilverPohligHellman(Screen):
	def __init__(self, **kwargs):
		super(SilverPohligHellman, self).__init__(**kwargs)

		
		self.tip = Label(text="Silver–Pohlig–Hellman algorithm which computes a discrete logarithms in a finite abelian group (g^x=y mod p)", 
		pos_hint={"right":0.85, "top":1}, size_hint=(0.8,0.1), halign="left", valign="middle")
		self.tip.bind(size=self.tip.setter("text_size"))
		self.add_widget(self.tip)
		
		self.tip1 = Label(text="Input g (it must be a generator):", size_hint=(0.3, 0.1), 
		pos_hint={"right":0.35, "top":0.93}, halign="left", valign="middle")
		self.tip1.bind(size=self.tip1.setter("text_size"))
		self.add_widget(self.tip1)
		
		self.data1 = TextInput(multiline=False, size_hint=(0.1, 0.05), pos_hint={"right":0.5, "top":0.9})
		self.add_widget(self.data1)
		
		self.tip2 = Label(text="Input y:", size_hint=(0.3, 0.1), 
		pos_hint={"right":0.35, "top":0.83}, halign="left", valign="middle")
		self.tip2.bind(size=self.tip2.setter("text_size"))
		self.add_widget(self.tip2)
		
		self.data2 = TextInput(multiline=False, size_hint=(0.1, 0.05), pos_hint={"right":0.5, "top":0.8})
		self.add_widget(self.data2)
		
		self.tip3 = Label(text="Input q (it must be a prime number):", size_hint=(0.3, 0.1), 
		pos_hint={"right":0.35, "top":0.73}, halign="left", valign="middle")
		self.tip3.bind(size=self.tip3.setter("text_size"))
		self.add_widget(self.tip3)
		
		self.data3 = TextInput(multiline=False, size_hint=(0.1, 0.05), pos_hint={"right":0.5, "top":0.7})
		self.add_widget(self.data3)
		
		self.btn = Button(text="Proceed!", size_hint=(0.2, None), pos_hint={"right":0.85, "top":0.9})
		self.btn.bind(on_press = self.action)
		self.add_widget(self.btn)
		
		self.answ = Label(text="", size_hint=(0.2, 0.1), pos_hint={"right":0.4, "top":0.6},
		halign="left", valign="middle")
		self.answ.bind(size=self.answ.setter("text_size"))
		self.add_widget(self.answ)
		
		
	def action(self, btn):
		answer = SPH(int(self.data1.text), int(self.data2.text), int(self.data3.text))
		self.answ.text = "Answer: x = " + str(answer)
		
		self.solve_btn = Button(text="Show solution", size_hint=(0.15, 0.1), 
		pos_hint={"right":0.5, "top":0.6})
		self.solve_btn.bind(on_press = self.solution)
		self.add_widget(self.solve_btn)
		
	def solution(self, btn):
		self.scroller = ScrollView(size_hint=(1, 0.45), pos_hint={"top":0.5})
		self.grid_layout = GridLayout(cols=1, spacing=5, size_hint_y=None, size_hint_x=0.5)
		self.grid_layout.bind(minimum_height=self.grid_layout.setter('height'))
		
		g=self.data1.text
		y=self.data2.text
		p=self.data3.text
		
		congr = Label(text="{}^x = {} mod{}".format(g, y, p), height=30, size_hint_y=None)
		self.grid_layout.add_widget(congr)
		
		factorization = factorize(int(p)-1)
		
		factor = Label(text="q-1 = "+str(factorization), height=30, size_hint_y=None)
		self.grid_layout.add_widget(factor)
		
		#print system of linear congruencies
		for pr in set(factorization):
			x_list=[]
			for power in range(0, factorization.count(pr)):
				x_list.append(str(pr**(power))+"x[{}]".format(power))
			linear_congr=Label(text="x = " + "+".join(x_list) + " mod{}".format(pr**factorization.count(pr)), height=20, size_hint_y=None, halign="left")
			linear_congr.bind(size=linear_congr.setter("text_size"))
			self.grid_layout.add_widget(linear_congr)
		
		sys_list=[]
		
		for pr in set(factorization):
			pr_num=Label(text="p = {}:".format(pr), height=30, size_hint_y=None)#print current p from factor list
			self.grid_layout.add_widget(pr_num)
			
			r_list = [int(g)**(int((int(p)-1)*j/pr))%int(p) for j in range(pr)]
			temp_y = int(y)
			r_counter=0
			y_counter=0
			sum_x_list=[]
			
			#print list of r-values
			for r_val in r_list:
				r=Label(text="r[{},{}] = ".format(pr,r_counter)+"{}".format(r_val), height=20, size_hint_y=None, halign="left")
				r.bind(size=r.setter("text_size"))
				self.grid_layout.add_widget(r)
				r_counter+=1
			
			#print y-values
			for power in range(1, factorization.count(pr)+1):	
				for r_val in r_list:
					if temp_y**int((int(p)-1)/pr**power)%int(p) == r_val:
						y_cur=Label(text="y[{}]={}".format(y_counter,temp_y), height=30, size_hint_y=None, halign="left")
						y_lbl=Label(text="{}^{} = {} mod{}".format(temp_y,int((int(p)-1)/pr**power),r_val,int(p)), height=30, size_hint_y=None, halign="left")
						x_lbl=Label(text="Then x[{}]={}".format(y_counter,r_list.index(r_val)), height=30, size_hint_y=None, halign="left")
						y_cur.bind(size=y_cur.setter("text_size"))
						y_lbl.bind(size=y_lbl.setter("text_size"))
						x_lbl.bind(size=x_lbl.setter("text_size"))
						self.grid_layout.add_widget(y_cur)
						self.grid_layout.add_widget(y_lbl)
						self.grid_layout.add_widget(x_lbl)
						sum_x_list.append(r_list.index(r_val)*pr**(power-1))
						break
				temp_y = (temp_y*inversed_el(int(g)**(pr**(power-1)*r_list.index(r_val)), int(p)))%int(p)
				y_counter+=1		
			
			res = sum(sum_x_list)%(pr**factorization.count(pr))
			sys_list.append([res, pr**factorization.count(pr)])
		
		#print system of congruencies we obtain
		self.grid_layout.add_widget(Label(text="So, the system of congrunecies:", height=30, size_hint_y=None))
		
		for i in range(len(set(factorization))):
			final_congr=Label(text="x={} mod{}".format(sys_list[i][0],sys_list[i][1]), height=20, size_hint_y=None, halign="left")
			final_congr.bind(size=final_congr.setter("text_size"))
			self.grid_layout.add_widget(final_congr)
			
		result=Label(text="x={} mod{}".format(sys_of_linear_congrs(sys_list), int(p)-1), height=30, size_hint_y=None)
		self.grid_layout.add_widget(result)
		
		self.scroller.add_widget(self.grid_layout)
		self.add_widget(self.scroller)
		

class ScreenManagement(ScreenManager):
	pass

	
presentation = Builder.load_file("Algorithm.kv")


class AlgorithmApp(App):
	def build(self):
		return presentation
		
if __name__ == "__main__":
	AlgorithmApp().run()
	
	
	
	
	
	