class Matrix:
	__matrix = []

	def __init__(self, matrix_str):
		try:
			self.__matrix = list(
				map(
					lambda x: list(map(lambda y: float(y), x)),
					map(lambda i: i.split(" "), matrix_str.split("\n"))
				)
			)
		except Exception:
			pass

	def getRow(self, index):
		if index < len(self.__matrix):
			return self.__matrix[index]

		return []

	def getColumn(self, index):
		try:
			return [ self.__matrix[i][index] for i in range(len(self.__matrix)) ]
		except Exception:
			return []




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
			print(matrix.getColumn(int(input("column's index: "))))
		elif get == 'r':
			print(matrix.getRow(int(input("row's index: "))))


	