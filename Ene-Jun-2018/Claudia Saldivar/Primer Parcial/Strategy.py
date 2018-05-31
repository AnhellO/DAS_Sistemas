class Panel:
    def __init__(self, form):
        if form:
             self.execute = form

    def execute(self):
        print("Original execution")

def executeButton():
    print("Button")

def executeList():
    print("List")

if __name__ == "__main__":
    strat0 = Panel()
    strat1 = Panel(executeButton)
    strat2 = Panel(executeList)

    strat0.execute()
    strat1.execute()
    strat2.execute()
