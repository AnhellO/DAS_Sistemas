# 6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 102)
# by replacing your series of print statements with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
        'str': 'A kind of object related with series of characters.',
        'list': 'A collection of items.',
        'comments': 'Notes in a program.',
        'insert': "It's used for adding something, for example in a list.",
        'del': "It's used for delete something, for example in a list.",

        'value': 'An item associated with a key in a dictionary.',
        'key': 'The first item in a key-value pair in a dictionary.',
        'boolean': 'An expression that evaluates to True or False.',
        'float': 'A numerical value with a decimal component.',
        'conditional': 'A comparison between two values.',
           }

for word, definition in glossary.items():
    print("\n" + word.title() + ": " + definition)