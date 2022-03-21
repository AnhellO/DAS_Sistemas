from page_builder import PageBuilder


class Page:
    def __init__(self,
                 path,
                 url):
        self._PATH = path
        self._URL = url
        self._title = ""
        self._headers = []         # list of headers
        self._paragraphs = []      # list of paragraphs
        self._hyperlinks = []      # list of hyperlinks
        self._lists = []           # lists in python of html lists
        self._scripts = []         # list of scripts
        self._css = []             # list of css
        self._images = []          # list of images

    # Attributes getters and setters
    @property
    def path(self):
        return self._PATH

    @path.setter
    def path(self, value):
        self._PATH = value

    @property
    def url(self):
        return self._URL

    @url.setter
    def url(self, value):
        self._URL = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def headers(self):
        return self._headers

    @headers.setter
    def headers(self, value):
        self._headers = value

    @property
    def paragraphs(self):
        return self._paragraphs

    @paragraphs.setter
    def paragraphs(self, value):
        self._paragraphs = value

    @property
    def hyperlinks(self):
        return self._hyperlinks

    @hyperlinks.setter
    def hyperlinks(self, value):
        self._hyperlinks = value

    @property
    def lists(self):
        return self._lists

    @lists.setter
    def lists(self, value):
        self._lists = value

    @property
    def scripts(self):
        return self._scripts

    @scripts.setter
    def scripts(self, value):
        self._scripts = value

    @property
    def css(self):
        return self._css

    @css.setter
    def css(self, value):
        self._css = value

    @property
    def images(self):
        return self._images

    @images.setter
    def images(self, value):
        self._images = value

    def __str__(self):
        msg = f"\t|| Page Information ||\n"
        msg += f"* PATH: {self._PATH}\n"
        msg += f"* URL: {self._URL}\n"
        msg += f"* Title: {self._title}\n"
        msg += f"* Headers: {self._headers}\n"
        msg += f"* Paragraphs: {self._paragraphs}\n"
        msg += f"* Hyperlinks: {self._hyperlinks}\n"
        msg += f"* Lists: {self._lists}\n"
        msg += f"* Scripts: {self._scripts}\n"
        msg += f"* CSS: {self._css}\n"
        msg += f"* Images: {self._images}\n"
        return msg


class ConcretePageBuilder(PageBuilder):
    def __init__(self, path, url):
        self._page = Page(path, url)

    def set_title(self, title):
        self._page.title = title
        return self

    def add_header(self, header):
        self._page.headers.append(header)
        return self

    def add_paragraph(self, paragraph):
        self._page.paragraphs.append(paragraph)
        return self

    def add_hyperlink(self, hyperlink):
        self._page.hyperlinks.append(hyperlink)
        return self

    def add_list(self, list):
        self._page.lists.append(list)
        return self

    def add_script(self, script):
        self._page.scripts.append(script)
        return self

    def add_CSS(self, css):
        self._page.css.append(css)
        return self

    def add_images(self, image):
        self._page.images.append(image)
        return self

    def build(self):
        return self._page
