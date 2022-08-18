from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_product_to_basket(self):
        busket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        busket_button.click()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Basket button is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"

    def should_be_same_product_title_after_basket_add(self):
        assert self.is_text_of_elements_equal((ProductPageLocators.PRODUCT_TITLE,
                                                ProductPageLocators.PRODUCT_TITLE_IN_MESSAGE)), "Products titles are different"

    def should_be_same_product_price_after_basket_add(self):
        assert self.is_text_of_elements_equal((ProductPageLocators.PRODUCT_PRICE,
                                                ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE)), "Products prices are different"

