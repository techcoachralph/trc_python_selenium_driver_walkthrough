from selenium.webdriver.common.by import By
from citronella import ui

class RestaurantDetails:
    def restaurant_name(self):
        return ui(By.CSS_SELECTOR, "main h1")

