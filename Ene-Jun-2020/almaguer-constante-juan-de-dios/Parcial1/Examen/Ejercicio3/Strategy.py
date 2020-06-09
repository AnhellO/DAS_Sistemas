import requests
import abc
from Ejercicio1 import Pages


# Se define la clase Reponse, encargada de recibir objetos Page

class Response:
    def __init__(self, page):
        self.page = page

    # Evalua el tipo de formato del objeto Page e implementa una estrategia diferente segun el formato
    def context(self):
        if self.page.get_formato() == 'HTML':
            response = htmlStrategy.content(self.page)
            return response

        if self.page.get_formato() == 'XML':
            response = xmlStrategy.content(self.page)
            return response

        if self.page.get_formato():
            response = jsonStrategy.content(self.page)
            return response


# Se define la Clase de la que van a heredar las estrategias
class ContentStrategy(metaclass=abc.ABCMeta):

    def response(self):
        pass


class htmlStrategy(ContentStrategy):

    def content(self):
        response = requests.get(self.get_url())
        return f'Response:\n Page: {self.get_url()}\n ' \
               f'Type: {self.get_formato()}\n ' \
               f'Content: {response.content}'


class xmlStrategy(ContentStrategy):

    def content(self):
        response = requests.get(self.get_url())
        return f'Response:\n Page: {self.get_url()}\n ' \
               f'Type: {self.get_formato()}\n ' \
               f'Content: {response.content}'


class jsonStrategy(ContentStrategy):

    def content(self):
        response = requests.get(self.get_url())
        return f'Response:\n Page: {self.get_url()}\n ' \
               f'Type: {self.get_formato()}\n ' \
               f'Content: {response.json()}'


if __name__ == '__main__':
    # Creacion de objetos de tipo Page
    child_page = Pages.Page(url="http://www.gotmilk.com/every-child-is-unique-special-different/",
                            titulo="Every Child is Unique, Special, Different - Got Milk",
                            met_des="", formato="HTML")

    calcium_page = Pages.Page(url="http://www.gotmilk.com/kids-calcium-and-kale/",
                              titulo="Kids, Calcium and…12 cups of Kale? - Got Milk",
                              met_des="", formato="HTML")

    fake_page = Pages.Page(url="https://www.gotmilk.com/calcium-for-adults/",
                           titulo="Adults and Calcium Together",
                           met_des="Importance for Calcium in Adults could be significant", formato="XML")

    response1 = Response(child_page)
    response2 = Response(fake_page)

    response1.context()
    response2.context()
