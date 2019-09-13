#Fuente: https://gist.github.com/jasper-lyons/8557701
########## The Factory's base class #########
class AbstractFactory(object):

  def create_product(self, **args):
    raise NotImplementedError("Requires derived factory class for implementation.")


######### The class of the object that needs creating ###########
class Product(object):

  def do_somthing(self):
    print "Doing some things!"


######### The  Factory of the class that needs creating ###########
class ConcreteFactory(AbstractFactory):

  def create_product(self):
    return Product()


######### The class that needs a product ###########
class Client(object):

    def __init__(self, factory):
      self.factory = factory

    def use_a_product(self):
      product = self.factory.create_product()
      product.do_somthing()


######## Start le program #########
def main():
  factory = ConreteFactory()
  client = Client(factory)
  client.use_a_product()


######## Catch the start of the Program ########
if __name__ == "__main__":
main()
