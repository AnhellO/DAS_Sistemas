## 1.-  ¿qué pasaría con esa escalera if-elif y en específico con la clase Animal si vamos agregando más especies de animales?

> la escalera if-elif seguirá creciendo conforme se vaya agregando mas animales a la lista,

>en el caso de la clase animal y como se esta el código no es necesario usar la clase animal y obtener el nombre del animal ya que con solo poner el nombre del animal en la lista funcionaria el código y modificando en la escalera if
- ejemplo: 
``` 
animales = [
    'león',
    'ratón'
]

def sonido_animal(animales: list):
    for animal in animales:
        if animal == 'león':
            print('roar')

        elif animal == 'ratón':
            print('squeak')

sonido_animal(animales)
```
- y el metodo :
```
def get_nombre(self) -> str:
    pass
```
> no se utiliza por lo que es codigo basura codigo muerto
por lo que la clase animal si le agregamos más animales
no afectaria mas que podria simplificarse y eviar el codigo muerto