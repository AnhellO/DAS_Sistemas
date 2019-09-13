class TextEditor:
    _content = ''

    def type(self, words):
        self._content = self._content + ' ' + words

    def get_content(self):
       return self._content.strip()


editor = TextEditor()
editor.type('This is the first sentence')
editor.type('This is the second.')
print(editor.get_content())