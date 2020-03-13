import abc


class Page(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def url(self):
        pass

    def path(self):
        pass

    def link(self):
        pass

    def titulo(self):
        pass

    def descripcion(self):
        pass

    def formato(self):
        pass


class form_html(Page):
    def __init__(self, texto):
        self._lineadtxt = texto

    # funciones
    def url(self):
        return 'https://es.wikipedia.org/wiki/Wikipedia:Portada\n'

    def path(self):
        return 'Ayuda\n'

    def link(self):
        return 'https://es.wikipedia.org/wiki/Ayuda:Contenidos\n'

    def titulo(self):
        return 'Ayuda:Contenidos\n'

    # funcion que regresa el texto ingresado que queremos decorar
    def desc(self):
        return self._lineadtxt

    def formato(self):
        return '\nhtml'


class decor(Page, metaclass=abc.ABCMeta):
    def __init__(self, linetxt):
        self.line = linetxt

    def url(self):
        return 'https://es.wikipedia.org/wiki/Wikipedia:Portada\n'

    def path(self):
        return 'Ayuda\n'

    def link(self):
        return 'https://es.wikipedia.org/wiki/Ayuda:Contenidos\n'

    def titulo(self):
        return 'Ayuda:Contenidos\n'

    def desc(self):
        return self.line.desc() + '\n'

    def formato(self):
        return 'html'


class Decc(decor):
    def __init__(self, parr):
        decor.__init__(self, parr)

    # Se decora poniéndole color y alineando el texto
    def desc(self):
        return '<p style="color:blue; align-text: center">' + self.line.desc() + '</p>\n'


def main():

    html_fmt = form_html('Esta ayuda contiene enlaces a manuales y explicaciones que te facilitarán el día a día en Wikipedia.')
    print(html_fmt.url(), html_fmt.path(), html_fmt.link(), html_fmt.titulo(), html_fmt.desc(), html_fmt.formato())

    print('\n\nAHORA DECORADO :v\n\n')

    objDecorado = Decc(form_html('Esta ayuda contiene enlaces a manuales y explicaciones que te facilitarán el día a día en Wikipedia.'))
    print(objDecorado.url(), objDecorado.path(), objDecorado.link(), objDecorado.titulo(), objDecorado.desc(),
          objDecorado.formato())


if __name__ == '__main__':
    main()
