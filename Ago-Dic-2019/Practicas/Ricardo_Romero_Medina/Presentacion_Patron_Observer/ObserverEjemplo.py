class Observador:
     def __init__(self, name, subject):
         self.name = name
         subject.registrar(self)

     def notificar(self, evento):
         print (self.name, "el evento cambio", evento)
class Sujeto:
     def __init__(self):
         self.listeners = []
 
     def registrar(self, observador):
         self.listeners.append(observador)
 
     def eliminar(self, observador):
         self.listeners.remove(observador)
 
     def notificar_observador(self, event):
         for listener in self.listeners:
             listener.notificar(event)
subject = Sujeto()
listenerA = Observador("hola", subject)
listenerB = Observador("como estas", subject)

subject.notificar_observador("adios")
