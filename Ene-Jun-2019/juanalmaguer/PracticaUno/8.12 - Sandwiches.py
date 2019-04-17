def make_sandwich(*ingredients):
     """Summarize the pizza we are about to make."""
     print("\nMaking sandwich with the following ingredients:")
     for ingredient in ingredients:
      print("- " + ingredient)

make_sandwich( 'lettuce', 'ham', 'cheese')
make_sandwich( 'avocado', 'onion','tomato','pickles')
make_sandwich( 'ham')

