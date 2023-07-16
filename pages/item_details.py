from selenium.webdriver.common.by import By
from citronella import ui


class ItemDetails:
    def required_details_radio_button(self):
        return ui(By.ID, "Toggle-0")

    def save_item_configuration_button(self):
        return ui(By.CSS_SELECTOR, "div#prism-modal-footer button")

    def add_to_cart_button(self):
        return ui(By.CSS_SELECTOR, "button[data-anchor-id='AddToCartButton']")


def click_item_option_radio_button(content_page):
    print("Click on the item option radio")
    content_page.required_details_radio_button.click()


def click_add_to_cart_button(content_page):
    print("Click Add to cart button")
    content_page.add_to_cart_button.ec_visibility_of_element_located()
    content_page.add_to_cart_button.click()


def click_save_button_for_item_configuration(content_page):
    print("Click Save button")
    content_page.save_item_configuration_button.click()
