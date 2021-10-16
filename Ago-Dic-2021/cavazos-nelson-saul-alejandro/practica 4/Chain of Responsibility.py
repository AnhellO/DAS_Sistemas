from __future__ import annotations
from abc import ABC, abstractclassmethod, abstractmethod
import abc
from typing import Any, Optional

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler:Handler)-> Handler:
        pass
    @abstractmethod
    def handle(self,request)->Optional[str]:
        pass

class AbstractHandler(Handler):
    _next_handler:Handler= None
    def set_next(self, handler: Handler) -> Handler:
        self._next_handler=handler
        return handler
    @abstractmethod
    def handle(self, request:Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class tepigHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "Pokecubos":
            return f"tepig: se comera la {request}"
        else:
            return super().handle(request)

class EeveeHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "pokélitos":
            return f"Eevee: se comera la {request}"
        else:
            return super().handle(request)

class ElectabuzzHandler (AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "electricidad":
                return f"Electabuzz: se comera la {request}"
        else:
            return super().handle(request)

class  GyaradosHandlerr(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "carne":
                return f"Gyarados: se comera la {request}"
        else:
            return super().handle(request)

class  MunnaHandler(AbstractHandler):
    def handle(self, request: Any) -> str:
        if request == "sueños":
                return f"Munna: se comera la {request}"
        else:
            return super().handle(request)

def client_code(handler:Handler)->None:
    for food in ["carne","Pokecubos","tasa de cafe","pokélitos"]:
        print(f"\nEntrenador: quien quiere {food}?")
        result=handler.handle(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} nadie la quiso", end="")

if __name__ == "__main__":
   tepig= tepigHandler()
   eevee=EeveeHandler()
   Electabuzz=ElectabuzzHandler()
   Gyarados= GyaradosHandlerr()
   Munna=MunnaHandler()
   tepig.set_next(eevee).set_next(Electabuzz).set_next(Gyarados).set_next(Munna)

   print("cadena: tepig > Eevee > Electabuzz > Gyarados > Munna")
   client_code(tepig)
   print("\n")
   print ("sub cadena: Eevee > Electabuzz > Gyarados > Munna")
   client_code(eevee)
   print("\n")
   print ("sub cadena: Electabuzz > Gyarados > Munna")
   client_code(Electabuzz)
   print("\n")
   print ("sub cadena: Gyarados > Munna")
   client_code(Gyarados)
