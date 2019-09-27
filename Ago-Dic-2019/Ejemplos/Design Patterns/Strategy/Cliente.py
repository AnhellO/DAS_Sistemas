from SortContext import SortContext
from QuickSortStrategy import QuickSortStrategy
from ShellSortStrategy import ShellSortStrategy
from SelectionSortStrategy import SelectionSortStrategy
from MergeSortStrategy import MergeSortStrategy

def main():
	# sort_strategy = MergeSortStrategy()
	sort_context = SortContext(range(0, 100900))
	print(sort_context.sorted_list())

if __name__ == '__main__':
	main()