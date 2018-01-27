from holmium.core import facets, Page, Element, Section, Locators

class MySection(Section):
    required_element = Element(Locators.CLASS_NAME, "main_element", facet=True)
    optional_element = Element(Locators.CLASS_NAME, "secondary_element")

@facets.title(title='login page')
class LoginPage(Page):
    def do_login(self, username, password):
        .....

@facets.cookie(name="session")
@facets.defer(page=LoginPage, action=LoginPage.do_login, action_arguments= {"username":"ali", "password":"sekret"})
class ContentPage(Page):
    section = MySection(Locators.ID, "main-section")
