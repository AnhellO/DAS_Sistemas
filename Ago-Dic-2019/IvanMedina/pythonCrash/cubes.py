'''
Juan Ivan Medina Martinez
4.8
'''
from countingToTwenty import makeList


def cubes(list):
	for element in list:
		print(element**3)


if __name__ == "__main__":

    list=makeList(10)
    cubes(list)