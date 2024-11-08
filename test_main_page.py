from conftest import browser
from pages.main_page import MainPage

link = "https://sbis.ru/"

class TestTenzorPage:
    def test_check_first_case(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.check_first_scene_tenzor()

    def test_check_second_case(self,browser):
        page = MainPage(browser, link)
        page.open()
        page.check_second_scene_tenzor()