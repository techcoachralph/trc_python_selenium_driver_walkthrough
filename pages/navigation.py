from selenium.webdriver.common.by import By
from citronella import ui


class NavigationMenu:
    def item_count_in_cart(self):
        return ui(By.CSS_SELECTOR, "button[data-testid='OrderCartButton'] div[class] div")


def verify_amount_of_items_in_cart(content_page, expected_amount_of_items_in_cart):
    cart_count = content_page.item_count_in_cart.get_element().text
    assert cart_count == \
        f"{expected_amount_of_items_in_cart}", \
        f"Expected Items in Cart: {expected_amount_of_items_in_cart}\n" \
        f"Actual Items in Cart: {cart_count}"
