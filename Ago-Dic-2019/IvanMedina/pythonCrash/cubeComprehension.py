'''
Juan Ivan Medina Martinez
4.9
'''

def cubes(start,end,pow):
	
	list_cubes=[value**pow for value in range(start,end)]
    return list_cubes

if __name__ == "__main__":

    print(cubes(1,10,2))