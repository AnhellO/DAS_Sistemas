import abstract_factory as af
import unittest

class TestConsoleOnWindows(unittest.TestCase):
	def test_clear_windows_on_windows(self):
		self.assertEqual(af.WindowsFactory().get_clear_console().clear(), 0)

	def test_clear_linux_on_windows(self):
		self.assertEqual(af.LinuxFactory().get_clear_console().clear(), 1)

	def test_print_windows_on_windows(self):
		console = af.WindowsFactory().get_print_color()
		console.set_color("cyan")

		self.assertEqual(console.print("Texto generico"), 0)

	def test_print_linux_on_windows(self):
		console = af.LinuxFactory().get_print_color()
		console.set_color("cyan")

		self.assertEqual(console.print("Texto generico"), 1)

class TestConsoleOnLinux(unittest.TestCase):
	def test_clear_linux_on_linux(self):
		self.assertEqual(af.LinuxFactory().get_clear_console().clear(), 0)

	# == TEST FUNCIONAL SOLO EN LINUX ==
	#def test_clear_windows_on_linux(self):
	#	self.assertEqual(af.WindowsFactory().get_clear_console().clear(), 1)

	def test_print_linux_on_linux(self):
		console = af.LinuxFactory().get_print_color()
		console.set_color("cyan")

		self.assertEqual(console.print("Texto generico"), 0)

	# == TEST FUNCIONAL SOLO EN LINUX ==
	#def test_print_windows_on_linux(self):
	#	console = af.WindowsFactory().get_print_color()
	#	console.set_color("cyan")
	#
	#	self.assertEqual(console.print("Texto generico"), 1)

if __name__ == "__main__":
	unittest.main()
