'''
Juan Ivan Medina Martiniez
Exercise 5.4
'''
def alienColors2(yourColor,theColor):
	if yourColor==theColor:
	    score=5
	    print("Your score is {}".format(score))
	else:
		score=10
		print("Your score is {}".format(score))

if __name__ == '__main__':
	myColor="Green"
	theColor="Green"
	print("Your color is {}, Alien's color is {}.".format(myColor,theColor))
	alienColors2(myColor,theColor)
	myColor="Blue"
	print("Your color is {}, Alien's color is {}.".format(myColor,theColor))
	alienColors2(myColor,theColor)