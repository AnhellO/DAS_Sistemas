class Button:

    def __init__(self, submit_func, label):
        self.on_submit = submit_func
        self.label = label

button1 = Button(sum, "Add 'em")
button2 = Button(lambda nums: " ".join(map(str, nums)), "Join 'em")

numbers = range(5, 23)
print (button1.on_submit(numbers))
print (button2.on_submit(numbers))