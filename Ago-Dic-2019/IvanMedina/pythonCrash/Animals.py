'''
Juan Ivan Medina Martinez
4.2
'''
def animalsPhrases(list_animals, list_phrases):

	for i in range(0,len(list_phrases)):
		print(list_phrases[i].replace('animal',list_animals[i]))
	print("Any of theses animals would make a great pet!")



if __name__ == '__main__':
    list_animals=['Echidnas','Platypus','Whales']	
    list_phrases=[]
    list_phrases.append("have you heard about the animal")
    list_phrases.append("Hey, has anyone seen my animal?")
    list_phrases.append("I'm sorry, I'm allergic to animal")    
    animalsPhrases(list_animals,list_phrases)
    
