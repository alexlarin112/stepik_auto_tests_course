from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class MainPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, "span.btn-group > a.btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "form#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "input#id_registration-email.form-control")
    REGISTER_PASSWORD1 = (By.CSS_SELECTOR, "input#id_registration-password1.form-control")
    REGISTER_PASSWORD2 = (By.CSS_SELECTOR, "input#id_registration-password2.form-control")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    TITLE = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1) > .alertinner > strong")
    PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main p.price_color")
    PRICE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(3) > .alertinner > p > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > .alert:nth-child(1)")


class BasketPageLocators:
    EMPTY_BASKET_TEXT = (By.CSS_SELECTOR, "div#content_inner > p")
    BASKET_SUMMARY = (By.CSS_SELECTOR, "form.basket_summary")
