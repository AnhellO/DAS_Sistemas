# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.

# • Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon
# and then its meaning, or print the word on one line and then print its meaning indented on a second line.
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'str': 'A kind of object related with series of characters.',
    'list': 'A collection of items.',
    'comments': 'Notes in a program.',
    'insert': "It's for add something in a list.",
    'del': "It's for delete something in a list.",
    }

word = 'str'
print("\n" + word.title() + ": " + glossary[word])

word = 'list'
print("\n" + word.title() + ": " + glossary[word])

word = 'comments'
print("\n" + word.title() + ": " + glossary[word])

word = 'insert'
print("\n" + word.title() + ": " + glossary[word])

word = 'del'
print("\n" + word.title() + ": " + glossary[word])