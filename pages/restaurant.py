from selenium.webdriver.common.by import By
from citronella import ui

class RestaurantDetails:
    def restaurant_name(self):
        return ui(By.CSS_SELECTOR, "main h1")

    def first_popular_menu_item(self):
        return ui(By.CSS_SELECTOR, "div[data-anchor-id='MenuItem']")

def click_on_first_popular_menu_item(content_page):
    content_page.first_popular_menu_item.click()
