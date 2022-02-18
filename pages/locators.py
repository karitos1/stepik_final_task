from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    OPEN_BASKET_BTN = (By.CSS_SELECTOR, ".basket-mini .btn.btn-default")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_ADDED_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    ADDED_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alertinner p strong")
    ADDED_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages strong")


class BasketPageLocators:
    PRODUCTS = (By.CLASS_NAME, "basket-items")
    EMPTY_BASKET_TEXT = (By.XPATH, "//div[@id='content_inner']/p")
