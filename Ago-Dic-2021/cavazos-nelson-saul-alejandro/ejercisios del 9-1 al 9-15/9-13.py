from collections import OrderedDict
glosario=OrderedDict()
glosario['Dictionary']="obra donde se puede consultar palabras o términos y se proporciona su significado"
glosario['key']="palabra calve en el diccionario que sirve para encontrar el significado "
glosario['values']="valores que se les da a un objeto"
glosario['alien']="ser vivo que no vive en el planeta tierra"
glosario['color']="reflejo de la luz que es percibido por el ojo humano"

for name, significado in glosario.items():
    print(name.title()+": "+significado.title())