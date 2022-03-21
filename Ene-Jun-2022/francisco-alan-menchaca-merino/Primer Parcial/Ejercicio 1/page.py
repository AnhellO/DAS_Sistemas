# Class which simulates a WebPage
class Page:
    def __init__(self,
                 path,
                 url,
                 title,
                 headers,
                 paragraphs,
                 hyperlinks,
                 lists,
                 scripts,
                 css,
                 images):
        self._PATH = path
        self._URL = url
        self._title = title
        self._headers = headers         # list of headers
        self._paragraphs = paragraphs   # list of paragraphs
        self._hyperlinks = hyperlinks   # list of hyperlinks
        self._lists = lists             # lists in python of html lists
        self._scripts = scripts         # list of scripts
        self._css = css                 # list of css
        self._images = images           # list of images

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

    # String representation of the object
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
