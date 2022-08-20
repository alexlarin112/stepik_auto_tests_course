from .locators import ProductPageLocators, MainPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_basket_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRICE), "Product price is not presented"

    def should_be_product_title(self):
        assert self.is_element_present(*ProductPageLocators.TITLE), "Product price is not presented"

    def should_be_same_product_title_after_basket_add(self):
        assert self.browser.find_element(*ProductPageLocators.TITLE).text == \
               self.browser.find_element(*ProductPageLocators.TITLE_IN_MESSAGE).text, "Product titles are different"

    def should_be_same_product_price_after_basket_add(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_IN_MESSAGE).text, "Product prices are different"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should disappeared"

    def should_be_basket_button(self):
        assert self.is_element_present(*MainPageLocators.BASKET_BUTTON), \
            "The Basket button is not presented"

    def go_to_basket_page_by_basket_button(self):
        self.browser.find_element(*MainPageLocators.BASKET_BUTTON).click()






