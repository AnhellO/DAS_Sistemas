from page import Page
from website import Website


def searcher(website, page_name):
    if page_name in website._pages.keys():
        page = website._pages[page_name]
    return page


if __name__ == "__main__":
    # Crating an instance of the class Page
    page = Page(
        "C:\\Users\\Alan\\website",
        "https://www.xataka.com.mx/menu",
        "Xataka México",
        ["<h1>header 1</h1>", "<h2>header 2</h2>", "<h3>header 3</h3>"],
        ["<p>Paragraph 1</p>", "<p>Paragraph 2</p>",
            "<p>Paragraph 3</p>"],
        ["<a href=\"https://www.xataka.com.mx/about\">About this site</a>",
         "<a href=\"https://www.xataka.com.mx/FAQ\">For more information</a>"],
        ["<ol><li>list 1.1</li><li>list 1.2</li></ol>",
            "<ul><li>list 2.1</li><li>list 2.2</li></ul>"],
        ["<script>Script1</script>", "<script>Script2</script>"],
        ["<style>CSS1</style>", "<style>CSS2</style>", "<style>CSS3</style>"],
        ["<img src=\"pic_trulli.jpg\">", "<img src=\"img_girl.jpg\">"])
    # Printing the string representation of the page object
    print(page)

    # Crating an instance of the class Website
    website = Website(
        "https://www.xataka.com.mx/",
        "Website domain",
        "Website subdomain",
        "Website hosting",
        "type - news",
        "Privacy policy ....",
        {"page_menu": page})
    # Printing the string representation of the website object
    print(website)

    page_menu = searcher(website, "page_menu")
    print(page_menu)
