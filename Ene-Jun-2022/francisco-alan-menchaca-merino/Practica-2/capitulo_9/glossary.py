# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.

# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing your series of print
# statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your
# glossary. When you run your program again, these new words and meanings
# should automatically be included in the output.

# 9-13. OrderedDict Rewrite: Start with Exercise 6-4 (page 108), where you
# used a standard dictionary to represent a glossary. Rewrite the program using
# the OrderedDict class and make sure the order of the output matches the order
# in which key-value pairs were added to the dictionary.

from collections import OrderedDict
# As of Python version 3.7, dictionaries are ordered.
# In Python 3.6 and earlier, dictionaries are unordered.
glossary = OrderedDict()

glossary["variable"] = "Symbolic name that is a reference or pointer to an object."
glossary["list"] = "Data structure in Python that is a mutable, or changeable, ordered sequence of elements."
glossary["dictionary"] = "A dictionary is a collection which is ordered*, changeable and do not allow duplicates."
glossary["tuple"] = "Data structure that store an ordered sequence of values."
glossary["for_loop"] = "A for loop is used for iterating over a sequence."
glossary["indent"] = "Indentation refers to the spaces at the beginning of a code line."
glossary["string"] = "Strings are arrays of bytes representing Unicode characters."
glossary["method"] = "A method is a function that “belongs to” an object."
glossary["integer"] = "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."
glossary["float"] = "Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length."

for word, meaning in glossary.items():
    print(f"- {word.title()}: {meaning}\n")
