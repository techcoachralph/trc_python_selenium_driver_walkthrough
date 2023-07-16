import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, ui


class HomePage:
    def delivery_address_field(self):
        return ui(By.ID, "HomeAddressAutocomplete")

    def arrow_button_to_search_address(self):
        return ui(By.CSS_SELECTOR, "div[data-testid='LandingPageAddressSearch'] button")

def search_for_address(content_page, address):
    content_page.delivery_address_field.send_keys(address)
    time.sleep(3)
    content_page.arrow_button_to_search_address.click()
