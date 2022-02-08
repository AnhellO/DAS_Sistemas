def make_helado(Sabor, *Complementos):    
    """Mostrar el Helado."""    
    print("\nHelado de " + str(Sabor) +          
    " con los siguientes complementos:")    
    for complemento in Complementos:        
        print("- " + complemento)