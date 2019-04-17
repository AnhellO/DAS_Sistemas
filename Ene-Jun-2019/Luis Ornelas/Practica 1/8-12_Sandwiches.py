def sandwich(*ingredientes):
    print("\nIngredientes del Sandwich:")
    for ingrediente in ingredientes:
        print("- " + ingrediente)

sandwich('Jamon','Queso','Lechuga','Toamte')
sandwich('Queso','Mantequilla')
sandwich('Tocino','Carne','Salsa BBQ')