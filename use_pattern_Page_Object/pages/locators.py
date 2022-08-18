from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")