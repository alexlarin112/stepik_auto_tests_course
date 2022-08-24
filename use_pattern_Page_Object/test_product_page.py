from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"]


# links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        browser.implicitly_wait(5)
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.register_new_user()
        login_page.should_be_authorized_user()

    @pytest.mark.parametrize('link', links)
    def test_user_cant_see_success_message(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', links)
    def test_user_can_add_product_to_basket(self, browser, link):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
        page.should_be_basket_add_button()
        page.add_product_to_basket()
        # page.solve_quiz_and_get_code()
        page.should_be_same_product_title_after_basket_add()
        page.should_be_same_product_price_after_basket_add()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_add_button()
    page.go_to_basket_page_by_basket_button()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_empty_basket()
    basket_page.should_be_text_of_empty_basket_in_empty_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()
    page.should_be_basket_add_button()
    page.add_product_to_basket()
    # page.solve_quiz_and_get_code()
    page.should_be_same_product_title_after_basket_add()
    page.should_be_same_product_price_after_basket_add()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_add_button()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.parametrize('link', links)
def test_message_disappeared_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_add_button()
    page.add_product_to_basket()
    page.should_disappear_success_message()

