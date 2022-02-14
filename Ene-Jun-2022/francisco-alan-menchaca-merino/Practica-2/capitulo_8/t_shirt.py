""" 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and
the text of a message that should be printed on the shirt. The function should
print a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the 
function a second time using keyword arguments. """


def make_shirt(size, text):
    print(f"Making a shirt of {size} size and "
          + f"with the text \"{text}\" printed on the shirt.")


make_shirt("small", "Hello World!")
# Making a shirt of small size and with the text "Hello World!" printed on the shirt.

make_shirt(size="medium", text="Python Crash Course")
# Making a shirt of medium size and with the text "Python Crash Course" printed on the shirt.
