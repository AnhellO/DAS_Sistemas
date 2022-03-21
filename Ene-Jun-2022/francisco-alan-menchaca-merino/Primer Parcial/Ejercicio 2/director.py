class Director:
    def __init__(self):
        self._builder = None

    # builder getter and setter
    @property
    def builder(self):
        return self._builder

    @builder.setter
    def builder(self, builder):
        self._builder = builder

    def fb_check_in_page(self):
        self._builder.set_title("Check-in")
        self._builder.add_paragraph(
            "<p>Paragraph 1</p>").add_paragraph("<p>Paragraph 2</p>")
        self._builder.add_hyperlink(
            "<a href=\"https://www.facebook.com/about\">About this site</a>")
        self._builder.add_script("<script>Script1</script>")
        self._builder.add_CSS("<style>CSS1</style>")
        self._builder.add_images("<img src=\"check_in.png\">")

    def openAI_check_in_page(self):
        self._builder.set_title("Check-in")
        self._builder.add_header("<h1>Check-in header1<\h1>")
        self._builder.add_paragraph("<p>Paragraph 1</p>")
        self._builder.add_hyperlink(
            "<a href=\"https://www.openai.com/about\">About this site</a>")
        self._builder.add_script("<script>Script1</script>")
        self._builder.add_script("<script>Script2</script>")
        self._builder.add_CSS("<style>CSS1</style>")
        self._builder.add_images("<img src=\"check_in_img.png\">")
        self._builder.add_images("<img src=\"openai_logo.png\">")
