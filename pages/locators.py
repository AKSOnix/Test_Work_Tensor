from selenium.webdriver.common.by import By

class MainPageLocators:
    CONTACTS = (By.XPATH, "//div[contains(text(), 'Контакты')]")
    MODAL_LINK = (By.XPATH, "//span[contains(text(), 'в России')]")
    IMG_TENZOR = (By.XPATH, "//img[contains(@alt, 'Разработчик системы СБИС')]")
    BLOCK_THIS = (By.XPATH, '// p[contains(text(), "Сила в людях")] / ancestor::div[contains( @class , "s-Grid-col")]')
    BUTTON_ABOUT = (By.XPATH, '//p[contains(text(), "Сила в людях")]/..//a[contains(text(), "Подробнее")]')
    IMAGE_BLOCKS = (By.XPATH, '//img[@width="270"][@height="192"]')
    DEFAULT_REGION = (By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text sbis_ru-link"]')
    PARTNERS_REGION =  (By.XPATH, '//div[@class="sbisru-Contacts-List__name sbisru-Contacts-List--ellipsis sbisru-Contacts__text--md pb-4 pb-xm-12 pr-xm-32"]')
    ENTER_REGION = (By.XPATH, '//span[@title="Камчатский край"]')
    PARTNERS_SELECT_REGION = (By.XPATH, '//div[@title="СБИС - Камчатка"]')