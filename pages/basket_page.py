from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS), "Basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), "No text of empty basket"
