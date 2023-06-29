import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
browser = webdriver.Chrome(
      options=chrome_options,
      service=ChromeService(ChromeDriverManager().install()))

# open it the door dash website
browser.get("http://www.doordash.com/")

# enter delivery address
# 5401 W Copans Rd, Margate, FL 33063
browser.find_element(By.ID, "HomeAddressAutocomplete").send_keys("5401 W Copans Rd, Margate, FL 33063")
time.sleep(5)
browser.find_element(By.CSS_SELECTOR, "div[data-testid='LandingPageAddressSearch'] button").click()
time.sleep(10)
# click fast food icon
browser.find_element(By.XPATH, "//span[.='Fast Food']").click()
time.sleep(10)
# click on the first restaurant
browser.find_element(By.CSS_SELECTOR, "a[data-anchor-id='StoreCard']").click()
time.sleep(10)
# print out the name of the restaurant
restaurant_name = browser.find_element(By.CSS_SELECTOR, 'main h1')
assert restaurant_name.is_displayed(), "Restaurant name not displayed"
print(f"Restaurant Selected is: "
      f"{restaurant_name.text}")

# view the menu
# browser.find_element(By.CSS_SELECTOR, "main button[kind='BUTTON/PRIMARY']").click()
browser.execute_script("window.scrollTo(0, 1000)")
time.sleep(3)
browser.execute_script("window.scrollTo(0, 1000)")
time.sleep(3)
# click on the first popular item
browser.find_element(By.CSS_SELECTOR, "div[data-anchor-id='MenuItem']").click()

# cart count
cart_count = browser.find_element(By.CSS_SELECTOR, "button[data-testid='OrderCartButton'] div[class] div").text
assert cart_count == "0", "Expected Items in Cart: 0\n" \
                          f"Actual Items in Cart: {cart_count}"

time.sleep(10)
# add the item to the cart
# required_options_list_size = len(browser.find_elements(
#     By.XPATH,
#     "//div[@data-testid='itemBody']//div[@aria-labelledby='optionList_Choose Size']"
#     "//div[contains(@class,'InlineChildren__StyledInlineChildren')]//span[.='Required']"))

# if required_options_list_size > 0:
#     browser.find_element(By.ID, "Toggle-0").click()
#     time.sleep(3)
#     # click save button for options
#     browser.find_element(By.CSS_SELECTOR, "div#prism-modal-footer button").click()
browser.find_element(By.ID, "Toggle-0").click()
time.sleep(3)
# click save button for options
browser.find_element(By.CSS_SELECTOR, "div#prism-modal-footer button").click()

time.sleep(2)
browser.find_element(By.CSS_SELECTOR, "button[data-anchor-id='AddToCartButton']").click()
time.sleep(3)
cart_count = browser.find_element(By.CSS_SELECTOR, "button[data-testid='OrderCartButton'] div[class] div").text
assert cart_count == "1", "Expected Items in Cart: 1\n" \
                          f"Actual Items in Cart: {cart_count}"

# close the browser
time.sleep(10)
# browser.quit()
