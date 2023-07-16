from selenium.webdriver.common.by import By
from citronella import ui


class SearchResults:
    def fast_food_in_filter(self):
        return ui(By.XPATH, "//span[.='Fast Food']")

    def first_restaurant(self):
        return ui(By.CSS_SELECTOR, "a[data-anchor-id='StoreCard']")


def filter_by_fast_food_category(content_page):
    content_page.fast_food_in_filter.click()


def choose_first_restaurant(content_page):
    content_page.first_restaurant.click()
