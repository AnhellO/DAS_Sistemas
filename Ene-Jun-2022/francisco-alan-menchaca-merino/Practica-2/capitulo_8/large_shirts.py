""" 8-4. Large Shirts: Modify the make_shirt() function so that shirts are
large by default with a message that reads I love Python. Make a large shirt
and a medium shirt with the default message, and a shirt of any size with a
different message. """


def make_shirt(size="large", text="I love Python"):
    print(f"Making a shirt of {size} size and "
          + f"with the text \"{text}\" printed on the shirt.")


make_shirt()
# Making a shirt of large size and with the text "I love Python" printed on the shirt.

make_shirt(size="medium")
# Making a shirt of medium size and with the text "I love Python" printed on the shirt.

make_shirt(size="small", text="Visual Studio 2022")
# Making a shirt of small size and with the text "Visual Studio 2022" printed on the shirt.
