class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name='', balance=0.0):
        """Return a Customer object whose name is *name* and starting
        balance is *balance*."""
        self.name = name
        self.balance = balance

    def set_name(self, name):
        """Sets the customer's name."""
        self.name = name
        return self

    def set_balance(self, balance):
        """Sets the customer's balance."""
        self.balance = balance
        return self

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

    def print_info(self):
        print('Name: %s\nBalance: %.2f\n' % (self.name, self.balance))


c = Customer('Angel', 100)
balance = c.deposit(200.50)
print('My current balance is: %.2f' % (balance))

balance = c.withdraw(50.50)
print('My current balance is: %.2f' % (balance))

c2 = Customer()
c2.set_name('Jacinto').set_balance(500.0).print_info()



