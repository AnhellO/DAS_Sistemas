type_words = ('texto en minusculas',)

class TextEditor(object):
    def __init__(self, type_words):
        self.type_words = type_words

class DefaultCaseState(TextEditor):
    for i in range(len(type_words)):
            print(type_words[i])

class UpperCaseState(TextEditor):
    for i in range(len(type_words)):
        if type_words[i].islower():
            print(type_words[i].upper())

class LowerCaseState(TextEditor):
    for i in range(len(type_words)):
        if type_words[i].isupper:
            print(type_words[i].lower())

class TitleCaseState(TextEditor):
    for i in range(len(type_words)):
        print(type_words[i].title())