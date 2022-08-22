from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_text_of_empty_basket_in_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT).text == \
               "Your basket is empty. Continue shopping", "Basket is empty, but text about it - is wrong or missing"

    def should_not_be_items_in_empty_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_SUMMARY), "Items in empty basket"
