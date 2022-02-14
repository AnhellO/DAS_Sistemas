def make_sandwich(*ingredientes):
    
    print("\nhare un rico sandwich:")
    for ingredientes in ingredientes:
        print("  agregando " + ingredientes + " al sandwich.")
    print("el sandwich esta listo!")

make_sandwich('queso', 'jamon', 'lechuga')
make_sandwich('tosino', 'pollo')
make_sandwich('tomate', 'aguacate')