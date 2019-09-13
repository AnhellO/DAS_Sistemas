name = input("Please enter your name: ")
print("Hello, " + name + "!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name= input(prompt)
print("\nHello, " + name + "!")

age = input("How old are you?")
print(age)

age = int(age)
print()

print(age>=15)