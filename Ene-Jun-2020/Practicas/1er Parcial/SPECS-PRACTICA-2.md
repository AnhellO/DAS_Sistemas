# Práctica 2

## Objetivo

Mejorar en el manejo básico de la POO en Python

## Especificaciones

#### Parte 1

* Crea una clase `Persona` en Python
  * La clase deberá de contener 5 propiedades, y 2 de esas propiedades deben de ser el peso y la estatura
  * Agregar constructor, `set`, `get` y `__str__` para la clase y sus propiedades
  * Agregar una función nueva que nos devuelva el IMC (Índice de Masa Corporal = `Peso / Estatura * Estatura`)

#### Parte 2

* Crea una clase `Empleado` que herede de la clase `Persona`
  * La nueva clase `Empleado` deberá de tener dos nuevos propiedades, una que sea el `ID` o número de empleado, y otro que indique la posición que este desempeña

#### Parte 3

* Crea una nueva clase `Empresa`
  * La clase deberá de contener tres diferentes propiedades que representen las características de una empresa, y adicionalmente, un cuarto atributo que contenga al conjunto de empleados que trabajan en la empresa. Todos los elementos de este conjunto deben de ser del tipo `Empleado`, de la clase creada en la parte anterior
  * Agrega una función de clase que añada nuevos empleados al conjunto de empleados que forman parte de la empresa
  * Agrega una función de clase que busque si un empleado con `ID` igual a `X` trabaja en la empresa
  * Agrega una función de clase que nos devuelva solamente los `IDs` o números de empleado de todo el conjunto de empleados que trabajan en la empresa

## Recursos

* Capítulos 8 y 9 del libro de `Python Crash Course`

## Deadline

* `Viernes 14 de Febrero a las 11:59pm`