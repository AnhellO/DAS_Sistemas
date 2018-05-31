import types
from tkinter import *
su = Tk()

su.geometry('300x300+200+300')
Label(root, text="Label a : x=0, y=0", bg="#FFFF00", fg="negro").place(x=0, y=0)
Label(root, text="Label b : x=50, y=40", bg="#3300CC", fg="blanco").place(x=40, y=30)
Label(root, text="Label c : x=75, y=80", bg="#FF0099", fg="negro").place(x=80, y=90)
Label(root, text="Label d : x=25, y=100", bg="#00FFFF", fg="blanco").place(x=30, y=120)
mainloop()

class tkinter:
	def __init__(self, func=None):
		self.name = 'Estrategia  0'
		if func is not None:
			self.ejecutar = types.MethodType(func, self)

	def ejecutar(self):
		print(self.name)

def ejecutar_reemplazo_1(self):
	print(self.name + 'de ejecutar 1')


if __name__ == '__main__':
	estrateg0 = tkinter()
	estrateg1 = tkinter(ejecutar_reemplazo_1)
	estrateg1.name = "Estrategia 1"
    estrateg0.ejecutar()
    estrateg1.ejecutar()