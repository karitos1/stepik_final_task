from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), \
            "Нет сообщения об успешном добавлении в корзину"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), \
            "Сообщения об успешном добавлении в корзину не должно быть"

    def should_disappear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_ADDED_TO_BASKET_MESSAGE), \
            "Сообщение об успешном добавлении в корзину не исчезло"

    def should_be_equal_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        added_product_name = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME)
        assert product_name.text == added_product_name.text, \
            "Название добавленного товара не совпадает с названием в сообщении."

    def should_be_equal_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        added_product_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE)
        assert product_price.text == added_product_price.text, \
            "Стоимость корзины не совпадает с ценой товара."


