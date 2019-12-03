'''
Juan Ivan Medina Martiniez
Exercise 5.5
'''
def alienColors3(yourColor,theColor1,theColor2,theColor3):
	if yourColor==theColor1:
	    score=5
	    print("Your score is {}".format(score))
	elif yourColor==theColor2:
		score=10
		print("Your score is {}".format(score))
	elif yourColor==theColor3:
		score=15
		print("Your score is {}".format(score))


if __name__ == '__main__':
	myColor="Green"
	theColor1="Green"
	theColor2="Yellow"
	theColor3="Red"
	myColor="Green"
	print("[+] Your alien's color is {}.".format(myColor))
	alienColors3(myColor,theColor1,theColor2,theColor3)
	myColor="Yellow"
	print("[+] Your alien's color is {}.".format(myColor))
	alienColors3(myColor,theColor1,theColor2,theColor3)
	myColor="Red"
	print("[+] Your alien's color is {}.".format(myColor))
	alienColors3(myColor,theColor1,theColor2,theColor3)
	myColor="Orange"
	print("[+] Your alien's color is {}.".format(myColor))
	alienColors3(myColor,theColor1,theColor2,theColor3)	
