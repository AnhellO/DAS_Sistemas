from page import ConcretePageBuilder as CPageBuilder
from website import ConcreteWebsiteBuilder as CWebsiteBuilder
from director import Director

if __name__ == "__main__":
    page_ = CPageBuilder("C:\\Users\\Alan\\website",
                         "https://www.xataka.com.mx/menu")
    page_.set_title("Xataka México")
    page_.add_header("<h1>header 1</h1>").add_header("<h2>header 2</h2>")
    page_.add_paragraph(
        "<p>Paragraph 1</p>").add_paragraph("<p>Paragraph 2</p>")
    page_.add_hyperlink(
        "<a href=\"https://www.xataka.com.mx/about\">About this site</a>")
    page_.add_list("<ol><li>list 1.1</li><li>list 1.2</li></ol>").add_list(
        "<ul><li>list 2.1</li><li>list 2.2</li></ul>")
    page_.add_script(
        "<script>Script1</script>").add_script("<script>Script2</script>")
    page_.add_CSS("<style>CSS1</style>").add_CSS("<style>CSS2</style>")
    page_.add_images("<img src=\"pic_trulli.jpg\">")
    builded_page = page_.build()
    print(builded_page)

    website_ = CWebsiteBuilder("https://www.xataka.com.mx/")
    website_.set_domain("Website domain").set_subdomain("Website subdomain")
    website_.set_hosting("Website hosting").set_website_type("type - news")
    website_.set_priv_policy("Privacy policy ...")
    website_.set_priv_policy({"page_menu": builded_page})
    builded_website = website_.build()
    print(builded_website)

    # Facebook check-in page
    check_in_page = CPageBuilder("C:\\Users\\Alan\\website",
                                 "https://www.facebook.com/check_in")
    director = Director()
    # FB predefined check-in page
    director._builder = check_in_page
    director.fb_check_in_page()
    fb_builded_page = director._builder.build()
    print(fb_builded_page)

    # OpenAI check-in page
    check_in_page = CPageBuilder("C:\\Users\\Alan\\website",
                                 "https://www.openai.com/check_in")
    # OpenAI predefined check-in page
    director._builder = check_in_page
    director.openAI_check_in_page()
    openAI_builded_page = director._builder.build()
    print(openAI_builded_page)
