# Parte 2

- **¿Qué busca solucionar esta arquitectura?**
Busca solucionar problemas relacionados con la organización de los scripts de una aplicación, así como la escalabilidad y facilitar el desarrollo con la clasificación de cada tipo de script

- **¿Qué es la "regla de dependencia" o "dependency rule"?**
Que las partes más internas del sistema no deben depender de las martes mas externas, sino al revés, esto porque las partes mpas internas manejan las bases de todo el sistema y por ello no cambian mucho, al contrario las partes externas son sometidas a muchos cambios constantemente para poder adaptarse a las necesidades de los clientes. 
- **¿Qué abarca la capa de Entidades o Entities?**
Los objetos de más alto nivel, la base del sistema completo.

- **¿Qué abarca la capa de Casos de Uso o Use Cases?**
Reglas de la aplicación, organizan el flujo de datos desde y hacia las entidades.

- **¿Qué abarca la capa de Adaptadores o Interface Adapters?**
Adaptan la información para ser manejada de forma apropiada por las distintas partes del sistema.

- **¿Qué abarca la capa de Frameworks o Frameworks and Drivers?**
Todas las cosas que necesita la aplicación para comunicarse y usar herramientas (BdD, UI, red, etc.)

- **¿Puede haber más de 4 capas? Complementa tu respuesta explicando tu razonamiento**
Probablemente, en lo personal no encuentro una razón para que haya más de 4 capas al seguir esta arquitectura ya que todas las herramientas que se me ocurren pueden ser clasificadas en una de las capas ya mencionadas. Sin embargo, no descarto la posibilidad de que algún día alguna persona describa una 4ta capa al aplicar una tecnología nueva.

- **¿Qué son los "boundaries"?**
Código que sirve como puente entre la aplicación y los servicios