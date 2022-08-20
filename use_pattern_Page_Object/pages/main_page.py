from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .base_page import BasePage
from .login_page import LoginPage


class MainPage(BasePage):
    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), \
            "The Basket button is not presented"

    def go_to_basket_page_by_basket_button(self):
        self.browser.find_element(*MainPageLocators.BASKET_BUTTON).click()
