from time import sleep
from .tenzor_page import TenzorPage
from .locators import MainPageLocators

class MainPage(TenzorPage):

    def check_first_scene_tenzor(self):
        link_contacts = self.browser.find_element(*MainPageLocators.CONTACTS)
        link_contacts.click()
        link_contacts = self.browser.find_element(*MainPageLocators.MODAL_LINK)
        link_contacts.click()
        link_contacts = self.browser.find_element(*MainPageLocators.IMG_TENZOR)
        link_contacts.click()
        original_window = self.browser.current_window_handle
        for window_handle in self.browser.window_handles:
            if window_handle != original_window:
                self.browser.switch_to.window(window_handle)
                break
        self.browser.execute_script("window.scrollTo(0, 500);")
        self.check_block()
        link_contacts = self.browser.find_element(*MainPageLocators.BUTTON_ABOUT)
        link_contacts.click()
        self.check_url()
        self.check_block_height_weight()

    def check_second_scene_tenzor(self):
        link_contacts = self.browser.find_element(*MainPageLocators.CONTACTS)
        link_contacts.click()
        link_contacts = self.browser.find_element(*MainPageLocators.MODAL_LINK)
        link_contacts.click()
        self.check_region_default()
        self.check_list_partners()
        link_contacts = self.browser.find_element(*MainPageLocators.DEFAULT_REGION)
        link_contacts.click()
        sleep(2)
        link_contacts = self.browser.find_element(*MainPageLocators.ENTER_REGION)
        link_contacts.click()
        sleep(2)
        self.check_select_region()
        self.check_url_select_region()
        self.check_partners_select_region()

