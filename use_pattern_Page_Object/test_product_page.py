from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()


def test_guest_should_see_basket_button(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_button()


def test_product_title_equals_product_title_in_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_same_product_title_after_basket_add()


def test_product_price_equals_price_in_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_same_product_price_after_basket_add()

