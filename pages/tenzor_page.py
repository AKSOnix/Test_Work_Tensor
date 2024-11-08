from .base_page import BasePage
from .locators import MainPageLocators

class TenzorPage(BasePage):
    def check_block(self):
        link_contacts = self.browser.find_element(*MainPageLocators.BLOCK_THIS)
        assert link_contacts

    def check_url(self):
        assert self.browser.current_url == 'https://tensor.ru/about'

    def check_block_height_weight(self):
        blocks = self.browser.find_elements(*MainPageLocators.IMAGE_BLOCKS)
        assert len(blocks) == 4

    def check_region_default(self):
        region = self.browser.find_elements(*MainPageLocators.DEFAULT_REGION)[0].text
        assert 'Свердлов' in region

    def check_list_partners(self):
        assert self.browser.find_elements(*MainPageLocators.PARTNERS_REGION)

    def check_select_region(self):
        assert 'Камчат' in self.browser.title

    def check_url_select_region(self):
        assert 'kamchat' in self.browser.current_url

    def check_partners_select_region(self):
        name_partner = self.browser.find_elements(*MainPageLocators.PARTNERS_SELECT_REGION)[0].text
        assert 'Камчат' in name_partner