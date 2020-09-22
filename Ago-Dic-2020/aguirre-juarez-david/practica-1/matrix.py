class Matrix:
	__matrix = []

	def __init__(self, matrix_str):
		self.__matrix = [m.split() for m in matrix_str.splitlines()]

	def get_row(self, index):
		return self.__matrix[index - 1]

	def get_column(self, index):
		return [ m[index - 1] for m in self.__matrix ]




if __name__ == '__main__':
	# get the input
	nrows = int(input("Number of rows: "))
	matrix_str = ""
	
	print("=== Write the matrix ===")
	for _ in range(nrows):
		matrix_str += f"{input()}\n"

	# get the matrix
	matrix = Matrix(matrix_str[0:-1])

	# get a row or column
	while True:
		get = input("column(c) or row(r)?: ")

		if get == 'c':
			print(matrix.get_column(int(input("column's index: "))))
		elif get == 'r':
			print(matrix.get_row(int(input("row's index: "))))