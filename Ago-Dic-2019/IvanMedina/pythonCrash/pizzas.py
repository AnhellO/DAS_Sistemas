'''
Juan Ivan Medina Martinez
4.1
'''


list_pizza=['Hawaiian Pizza','Pepperoni Pizza','Mexican Pizza']	

def pizzasPhrase(list_pizza, list_phrases):

	for i in range(0,len(list_phrases)):
		print(list_phrases[i].replace('pizza',list_pizza[i]))
	print("I really love pizza!")



if __name__ == '__main__':

    list_phrases=["Guess what we'll eat today?... pizza!","Anyone want to eat pizza?","I really need to eat pizza!"]
    pizzasPhrase(list_pizza,list_phrases)
        
