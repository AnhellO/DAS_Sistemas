import os

class ClearConsole:
	def clear(self):
		pass

class PrintColor:
	def set_color(self, color):
		pass
	
	def print(self, str):
		pass

class WindowsClearConsole(ClearConsole):
	def clear(self):
		return os.system("cls")
		
class LinuxClearConsole(ClearConsole):
	def clear(self):
		return os.system("clear")
		
class WindowsPrintColor(PrintColor):
	def __init__(self):
		self.__color_com = "color 0f"
	
	def set_color(self, color):
		color = color.capitalize()
		
		if color == "Red":
			self.__color_com = "color 04"
		elif color == "Lima":
			self.__color_com = "color 0a"
		elif color == "Cyan":
			self.__color_com = "color 0b"
		else:
			self.__color_com = "color 0f"

	def print(self, text):
		return os.system(f"{self.__color_com} && echo {text}")

class LinuxPrintColor(PrintColor):
	def __init__(self):
		self.__color_code = ""
	
	def set_color(self, color):
		color = color.capitalize()
		
		if color == "Red":
			self.__color_com = "\\033[31m"
		elif color == "Lima":
			self.__color_com = "\\033[32m"
		elif color == "Cyan":
			self.__color_com = "\\033[36m"
		else:
			self.__color_com = "\\033[39m"

	def print(self, text):
		return os.system(f"printf '{self.__color_com}{text}'")


class AbstractFactory:
	def get_clear_console(self):
		pass

	def get_print_color(self):
		pass

class LinuxFactory(AbstractFactory):
	def get_clear_console(self):
		return LinuxClearConsole()

	def get_print_color(self):
		return LinuxPrintColor()

class WindowsFactory(AbstractFactory):
	def get_clear_console(self):
		return WindowsClearConsole()

	def get_print_color(self):
		return WindowsPrintColor()