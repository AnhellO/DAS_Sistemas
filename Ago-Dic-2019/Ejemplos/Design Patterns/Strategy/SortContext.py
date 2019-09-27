from QuickSortStrategy import QuickSortStrategy
from ShellSortStrategy import ShellSortStrategy
from SelectionSortStrategy import SelectionSortStrategy
from MergeSortStrategy import MergeSortStrategy

class SortContext(object):
	"""docstring for SortContext"""
	def __init__(self, my_list, sort_strategy = None):
		self._my_list = my_list
		
		if sort_strategy != None:
			self._sort_strategy = sort_strategy
		else:
			list_lenght = len(my_list)
			if list_lenght < 100:
				self._sort_strategy = SelectionSortStrategy()
			elif list_lenght >= 100 and list_lenght < 10000:
				self._sort_strategy = ShellSortStrategy()
			elif list_lenght >= 10000 and list_lenght < 100000:
				self._sort_strategy = MergeSortStrategy()
			elif list_lenght >= 100000:
				self._sort_strategy = QuickSortStrategy()


	def sorted_list(self):
		return self._sort_strategy.sort(self._my_list)