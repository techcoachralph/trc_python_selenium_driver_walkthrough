import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from citronella import WebPage

from pages.content_page import ContentPage
from pages.home import HomePage
from pages.item_details import ItemDetails
from pages.navigation import NavigationMenu
from pages.restaurant import RestaurantDetails
from pages.search_results import SearchResults
from pages import home, search_results, restaurant, item_details, navigation

chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(
      options=chrome_options,
      service=ChromeService(ChromeDriverManager().install()))
web = WebPage(browser)
# open it the door dash website
web.driver.get("http://www.doordash.com/")


# create instance of each page object
web.page = ContentPage
home_page = web.page.home
search_results_page = web.page.search_results
restaurant_details_page = web.page.restaurant_details
item_details_page = web.page.item_details
navigation_page = web.page.navigation

# test starts
home.search_for_address(home_page, "5401 W Copans Rd, Margate, FL 33063")
time.sleep(3)

search_results.filter_by_fast_food_category(search_results_page)

search_results.choose_first_restaurant(search_results_page)

restaurant_name = restaurant_details_page.restaurant_name
restaurant_name.ec_visibility_of_element_located()
assert restaurant_name.get_element().is_displayed(), "Restaurant name not displayed"
print(f"Restaurant Selected is: "
      f"{restaurant_name.get_element().text}")

# scroll down on page
browser.execute_script("window.scrollTo(0, 1000)")
time.sleep(3)
browser.execute_script("window.scrollTo(0, 1000)")
time.sleep(3)

restaurant.click_on_first_popular_menu_item(restaurant_details_page)

navigation.verify_amount_of_items_in_cart(navigation_page, "0")
time.sleep(10)

item_details.click_item_option_radio_button(item_details_page)
time.sleep(2)
item_details.click_save_button_for_item_configuration(item_details_page)
time.sleep(2)
item_details.click_add_to_cart_button(item_details_page)
time.sleep(3)

navigation.verify_amount_of_items_in_cart(navigation_page, "1")

# close the browser
time.sleep(10)
# browser.quit()
