def make_sadwich(*items):
    print('Sandwich with :')
    for item in items:
        print(f"- {item}")
    print()        


make_sadwich('tomato')
make_sadwich('lettuce', 'chicken', 'ham')
make_sadwich('eggs', 'cheese', 'tomato', 'lettuce', 'ham')