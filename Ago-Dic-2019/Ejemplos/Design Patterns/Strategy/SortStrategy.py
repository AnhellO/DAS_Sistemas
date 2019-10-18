import abc

class SortStrategy(metaclass=abc.ABCMeta):
	"""docstring for SortStrategy"""
	@abc.abstractmethod
	def sort(self, my_list = []):
		pass