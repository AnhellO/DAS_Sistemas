# Implementa la funcionalidad necesaria utilizando el patrón de diseño Memento
# para que se pueda salvar el estado anterior del editor de texto, tal y como
# lo haría un editor real con el famoso "Undo". Debe de ser posible salvar ese
# estado, y regresar a el en cualquier momento durante la ejecución.

import pickle  # sirve para serlializar y deserializar objetos en python

class TextEditor:
    _content = ''  # inicializamos variable a ''

    def type(self, words):
        """Método para agregar texto a la variable _content"""
        self._content = self._content + ' ' + words

    def get_content(self):
       """Función que regresa el contenido de _content"""
       return self._content.strip()

    def create_memento(self):
        """Función que se encarga de serializar el objeto, lo guardamos"""
        return pickle.dumps(self._content)

    def set_memento(self, memento):
       """Método que se encarga de deserializar el objeto, eliminamos su
       contenido y actualizamos el contenido al estado anterior"""
       self._content = pickle.loads(memento)

# El patrón de diseño memento sirve para cambiar el estado de un objeto
# al estado anterior, como es el caso de los editores de texto con el CTRL+Z

def main():
    editor = TextEditor()  # creamos un objeto de la clase TextEditor
    editor.type('This is the first sentence')  # Escribimos el primer enunciado
    print(editor.get_content())  # Imprimimos el enunciado escrito
    memento = editor.create_memento()  # guardamos el texto
    editor.type('This is the second')  # Escribimos el segundo enunciado
    print(editor.get_content())  # Imprimimos el contenido total, es decir el
                                 # primer enunciado y el segundo
    editor.set_memento(memento)  # volvemos al estado anterior
    print(editor.get_content())  # Imprimimos el texto

if __name__ == "__main__":
    main()
