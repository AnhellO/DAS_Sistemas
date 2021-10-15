# Practica 4 - Patrón de Comportamiento: Strategy

## Sintesis comprendida

> Es un patron que sirve para encapsular logica, el objetivo es poder tener diferentes algoritmos para asi poder cambiar de una a otra de una forma mas facil.

> La clave esta en crear objetos que representen una estrategia que siga un mismo patron.

> El patron Strategy esta dividido en 5 elementos:
1. **Contexto:** Da una descripcion a las **estrategias concretas** y se comunica mendiante la **interfaz estategia**.

2. **Interfaz Estategia:** Es parecida a las concretas, declara un metodo que el **contexto** usa para el uso de una estrategia.

3. **Estrategias Concretas:** Utiliza la **interfaz estrategia** para que el **contexto** utilice y esta tenga una variacion de un algoritmo.

4. **Contexto:** Manda a llamar el objeto de estrategia vinculado cada que ejecuta un algoritmo, este no conoce la estrategia ni algoritmo.

5. **Cliente:** Este crea un objeto para darselo al **contexto** y este ejecute la estrategia requerida.

## Descripción del Ejemplo
> En este ejemplo se describe lo que ocurre en un juego de Futbol Americano: Decidi elegir esto para desarrollar el patron de diseño, pues de alguna manera se relaciona a una estrategia de juego dependiendo del contexto como es Yardaje, Numero de oportunidad y Yarda en campo.

> Como primer paso del codigo crearemos lo que seria nuestra interfaz para la estrategia
~~~
class ChoosePlayStrategy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def play(self):
        pass
~~~

> Despues de esto crearemos lo que seria nuestras estrategias concretas, en este caso usaremos 4
- Jugada por Pase
- Jugada por Tierra
- Intento de Gol de Campo
- Intento de Despeje
~~~
#Estrategia Concreta: Tierra
class rushPlayStrategy(ChoosePlayStrategy):
    def play(self):
        return 'Jugando por tierra'
~~~

> Luego de esto crearemos el contexto de la jugada
~~~
class playContext(object):
    def __init__(self, yardas, oportunidad, YardaCampo, strategy: ChoosePlayStrategy = None):
        self._yardas = yardas
        self._oportunidad = oportunidad
        self._YardaCampo = YardaCampo
        self._strategy = strategy
~~~
>En este caso como lo mencionamos anteriormente daremos como parametro lo que seria el yardaje, la posicon del balon en el campo y el numero de oportunidad, asi como su estrategia la cual en este caso estara nula.

> En este caso creamos 4 contextos para cada situacion los cuales serian
- Si la oportunidad es menor igual a 3 y las yardas a jugar son menor que 5, se jugara por tierra (En este caso no importa la posicion del balon)
- Si la oportunidad es igual a 4, las yardas mayor igual a 5 y la posicion del balon es menor a la yarda 70 iremos por intento de despeje
- Si la oportunidad es igual a 4, las yardas mayor igual a 1 y la posicion del balon es mayor a la yarda 70 iremos por intento de gol de campo

>En dado caso que no cumpla ninguna de las anteriores se jugara por aire
~~~
def play_context(self):

        if self._strategy != None:
            return self._strategy.play()

        if self._oportunidad <= 3 and self._yardas <= 5:
            return rushPlayStrategy.play(self)

        if self._oportunidad == 4 and self._yardas >= 5 and self._YardaCampo < 70:
            return puntPlayStrategy.play(self)

        if self._oportunidad == 4 and self._yardas >= 1 and self._YardaCampo >= 70:
            return fieldGoalPlayStrategy.play(self)

        return passPlayStrategy.play(self)

~~~
>Una vez realizado nuestras estrategias y contexto es hora de crear el cliente
~~~
yardas = randint(1, 15)
    oportunidad = randint(1, 4)
    yardasCampo = randint(1, 99)

    print(f'Oportunidad: {oportunidad}\n Yardas: {yardas}\n Balon en la yarda: {yardasCampo}')
    context = playContext(yardas, oportunidad, yardasCampo)
    print(context.play_context())
~~~
>En este caso estaremos dando un valor aleatorio para cada atributo y estos valores correrian la jugada
> En dado caso que nosotros queramos forzar una jugada por otra estrateigia debemos de mandar a llamar la estrategia por medio de la propiedad en el contexto "set_Strategy"
~~~
#Forzamos a jugar por tierra
    rushPlay = rushPlayStrategy()
    context.set_strategy(rushPlay)
    print(context.play_context())

~~~

## Diagrama UML

![Diagrama UML](https://imgur.com/a/Q7F1VAO)

## Referencias

Strategy. (2014). Refractoring Guru. https://refactoring.guru/es/design-patterns/strategy

Design Patterns and Refactoring. (2007). SourceMaking. https://sourcemaking.com/design_patterns/strategy/python/1

A. (2021, 5 febrero). The strategy pattern: write BETTER PYTHON CODE Part 3. YouTube. https://www.youtube.com/watch?v=WQ8bNdxREHU&feature=youtu.beB. 

(2020, 4 abril). STRATEGY | PATRONES de DISEÑO. YouTube. https://www.youtube.com/watch?v=VQ8V0ym2JSo&feature=youtu.be

Basado en el codigo de: TDD-DesignPaterns