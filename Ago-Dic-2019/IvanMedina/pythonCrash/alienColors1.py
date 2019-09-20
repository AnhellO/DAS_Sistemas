'''
Juan Ivan Medina Martiniez
Exercise 5.3
'''
def alienColors1(yourColor,theColor):
	if yourColor==theColor:
	    score=5
	    print("Your score is {}".format(score))

if __name__ == '__main__':
	myColor="Green"
	theColor="Green"
	print("Your color is {}, Alien's color is {}.".format(myColor,theColor))
	alienColors1(myColor,theColor)
	myColor="Blue"
	print("Your color is {}, Alien's color is {}.".format(myColor,theColor))
	alienColors1(myColor,theColor)