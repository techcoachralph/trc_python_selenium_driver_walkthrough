from selenium import webdriver
from selenium.webdriver.common.by import By
from citronella import WebPage, ui


class HomePage:
    def delivery_address_field(self):
        return ui(By.ID, "HomeAddressAutocomplete")

    def arrow_button_to_search_address(self):
        return ui(By.CSS_SELECTOR, "div[data-testid='LandingPageAddressSearch'] button")

    def search_for_address(self, address):
        self.delivery_address_field().send_keys(address)
        self.arrow_button_to_search_address().click()


