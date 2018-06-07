class TextRenderer(object):
    def __init__(self, text):
        self._text = text

    def render(self):
        return self._text

if __name__ == '__main__':
    renderer = TextRenderer("hello, pipol!")
    print(renderer.render())