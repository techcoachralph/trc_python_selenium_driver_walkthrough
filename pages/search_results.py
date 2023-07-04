from selenium.webdriver.common.by import By
from citronella import ui


class SearchResults:
    def fast_food_in_filter(self):
        return ui(By.XPATH, "//span[.='Fast Food']")

    def first_restaurant(self):
        return ui(By.CSS_SELECTOR, "a[data-anchor-id='StoreCard']")