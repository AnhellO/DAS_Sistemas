
def sandwich(*ingredients):
    
    print("Your sandwich will have:")
    
    for ingredient in ingredients:
        print("- " + ingredient)


sandwich('bread', 'jam', 'cheese')
sandwich('jam')
sandwich('jam','cheese','salchicha','onion','tomato','jam')