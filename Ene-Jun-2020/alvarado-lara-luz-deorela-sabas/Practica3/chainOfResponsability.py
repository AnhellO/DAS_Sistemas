class Account: 
    _successor = None
    _balance = None
    def set_NextMethod(self, account):
        self._successor = account
    def pay(self, amount_to_pay):
        instance_class_name = self.__class__.__name__
        if self.can_pay(amount_to_pay):
            print('Paid $' + str(amount_to_pay) + ' using ' + instance_class_name)
        elif self._successor:
            print('Cannot pay using ' + instance_class_name + '...')
            print('\t...checking next payment method')
            self._successor.pay(amount_to_pay)
        else:
            raise ValueError('None of the accounts have enough _balance')
    #define si la cantidad a pagar es menor que la cantidad de dinero existente en la cuenta
    def can_pay(self, amount: int):
        return self._balance >= amount
              
class Bitcoin(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance

class Paypal(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance

class Ecoin(Account):
    _balance = None

    def __init__(self, balance):
        self._balance = balance


if __name__ == '__main__':
    bitcoin = Bitcoin(100)
    paypal = Paypal(0)
    ecoin = Ecoin(1000)

    bitcoin.set_NextMethod(paypal)
    paypal.set_NextMethod(ecoin)

    bitcoin.pay(1000)
    