class Subscriber:
    def __init__(self, name):
        self.name = name
    def update(self, message):
        return '{} got message: "{}"\n'.format(self.name, message)
    def __str__(self):
        return "I'm {}".format(self.name)

class Publisher:
    def __init__(self):
        self.subscribers = set()
    def register(self, who):
        self.subscribers.add(who)
    def unregister(self, who):
        self.subscribers.discard(who)
    def dispatch(self, message):
        updates = ""
        for subscriber in self.subscribers:
            updates += subscriber.update(message)
        return updates

def main():
    pub = Publisher()
    bob = Subscriber('Bob')
    alice = Subscriber('Alice')
    john = Subscriber('John')
    pub.register(bob)
    pub.register(alice)
    pub.register(john)
    print(pub.dispatch('First update from publisher'))
    pub.unregister(alice)
    print(pub.dispatch('Second update from publisher'))

if __name__ == "__main__":
    main()