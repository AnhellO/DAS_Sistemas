
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

def print_models(unprinted_designs):


    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)
    return completed_models

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")

    for completed_model in completed_models:
        print(completed_model)
        
