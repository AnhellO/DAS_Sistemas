'''
Juan Ivan Medina Martinez
Exercise 5.7
'''

def favoriteFruit(fruitFavorites,fruit):
	if fruit in favorite_fruits:
		print("Hey you really like {}!".format(fruit))

if __name__ == '__main__':
    
    favorite_fruits=['banana','apple', 'pineapple','coconut','mango']
    fruit="strawberry"
    favoriteFruit(favorite_fruits,fruit)
    fruit="banana"
    favoriteFruit(favorite_fruits,fruit)
    fruit="cherry"
    favoriteFruit(favorite_fruits,fruit)
    fruit="coconut"
    favoriteFruit(favorite_fruits,fruit)
    fruit="pineapple"
    favoriteFruit(favorite_fruits,fruit)