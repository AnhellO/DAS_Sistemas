from abc import ABC, abstractmethod
class Interface(ABC):
    @abstractmethod
    def level_1_tasks(self, user: str, access_level):
        pass

    @abstractmethod
    def level_2_tasks(self, user: str, access_level):
        pass

    @abstractmethod
    def level_3_tasks(self, user: str, access_level):
        pass


class Concrete(Interface):
    def level_1_tasks(self, user: str):
        print(f"User {user} is doing level-1 task on system ### Payments ###")

    def level_2_tasks(self, user: str):
        print(f"User {user} is doing level-1 tasks on system ### IT ###")
        print(f"User {user} is doing level-2 tasks on system ### IT ###")

    def level_3_tasks(self, user: str):
        print(f"User {user} is doing level-1 tasks on system ### Sales ###")
        print(f"User {user} is doing level-2 tasks on system ### Sales ###")
        print(f"User {user} is doing level-3 tasks on system ### Sales ###")

class Proxy(Interface):
    def __init__(self):
        self._concrete = Concrete()

    def level_1_tasks(self, user: str, access_level):
        print(f"User {user} is doing level-1 task on system ### Payments ###")
        print(f"ERROR: User {user} is not authorized to do level-2 tasks")
        print(f"ERROR: User {user} is not authorized to do level-3 tasks")

    def level_2_tasks(self, user: str, access_level):
        print(f"User {user} is doing level-1 tasks on system ### IT ###")
        print(f"User {user} is doing level-2 tasks on system ### IT ###")
        print(f"ERROR: User {user} is not authorized to do level-3 tasks")

    def level_3_tasks(self, user: str, access_level):
        print(f"User {user} is doing level-1 tasks on system ### Sales ###")
        print(f"User {user} is doing level-2 tasks on system ### Sales ###")
        print(f"User {user} is doing level-3 tasks on system ### Sales ###")


if __name__ == "__main__":
    testo = Proxy()
    print(testo.level_1_tasks("foo", 1))
    print(testo.level_2_tasks("bar", 2))
    print(testo.level_3_tasks("baz", 3))