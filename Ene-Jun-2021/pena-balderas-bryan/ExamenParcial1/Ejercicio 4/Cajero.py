import abc

#En base al digrama y ejemplo visto en clase, creo las clases necesarias para el uso de chain of responsibility

#LA primera es la interface
class CajeroHandler(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def handle(self,cantidad):
        pass

    @abc.abstractmethod
    def set_next(self):
        pass

#creo la clase base de handler que tendra nuestros metodos de la interface y la logica
#para la secuencia de la cadena de pruebas
class BaseHandler(CajeroHandler):
    cantidades=""

    def set_next(self,next_handler:CajeroHandler):
        self.next=next_handler

    def handle(self, cantidad):
        if self.next!=None:
            return self.next.handle(cantidad)

#primer concrete el cual evalua el dinero en multiplos de 10
class Cajero10ConcreteHandler(BaseHandler):
    def handle(self, cantidad):
        if (cantidad % 10)==0:
            entrediez=cantidad//10
            restar=entrediez*10
            cantidad=cantidad-restar
            BaseHandler.cantidades=BaseHandler.cantidades+f" se usaron {entrediez} de 10 "
            return BaseHandler.cantidades

        return BaseHandler.cantidades
            
#segundo concrete el cual evalua en multiplos de 20
class Cajero20ConcreteHandler(BaseHandler):
    def handle(self, cantidad):
        if (cantidad % 20)!=0:
            entrediez=cantidad//20
            restar=entrediez*20
            cantidad=cantidad-restar
            BaseHandler.cantidades= BaseHandler.cantidades+ f" se usaron {entrediez} de 20 "
            return self.next.handle(cantidad)
        
        entrediez=cantidad//20
        cantidad=cantidad-entrediez
        BaseHandler.cantidades= BaseHandler.cantidades+ f" se usaron {entrediez} de 20 "
        return BaseHandler.cantidades

        
        
#tercer concrete el cual evalua en multiplos de 50
class Cajero50ConcreteHandler(BaseHandler):
    def handle(self, cantidad):
        BaseHandler.cantidades=''
        if (cantidad % 50)!=0:
            entrediez=cantidad//50
            restar=entrediez*50
            cantidad=cantidad-restar
            BaseHandler.cantidades= BaseHandler.cantidades+f" se usaron {entrediez} de 50 "
            return self.next.handle(cantidad)
        
        entrediez=cantidad//50
        cantidad=cantidad-entrediez
        BaseHandler.cantidades= BaseHandler.cantidades+f" se usaron {entrediez} de 50 "
        return BaseHandler.cantidades
        
        