import types
from tkinter import *
root = Tk()

root.geometry('200x200+100+200')

Label(root, text="Label 1 : x=0, y=0", bg="#FFFF00", fg="black").place(x=0, y=0)
Label(root, text="Label 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
Label(root, text="Label 3 : x=75, y=80", bg="#FF0099", fg="black").place(x=75, y=80)
Label(root, text="Label 4 : x=25, y=100", bg="#00FFFF", fg="white").place(x=25, y=100)

mainloop()

class tkinter:
	def __init__(self, func=None):
		self.name = 'Strategy  0'
		if func is not None:
			self.execute = types.MethodType(func, self)

	def execute(self):
		print(self.name)

def execute_replacement1(self):
	print(self.name + 'from execute 1')

def execute_replacement2(self):
	print(self.name + 'from execute 2')


if __name__ == '__main__':
	strat0 = tkinter()

	strat1 = tkinter(execute_replacement1)
	strat1.name = 'Strategy Example 1'

	strat2 = tkinter(execute_replacement2)
	strat2.name = 'Strategy Example 2'

	strat0.execute()
	strat1.execute()
	strat2.execute()

