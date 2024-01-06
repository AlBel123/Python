"""
Application name: Using Selenium for Cookies Game

Application Type: Selenium Utilization

Data of work start: 04 Jan 2024

Work finished: 05 Jan 2024

Application description:
The application allows to effectively use the opportunities of Cookies game at http://orteil.dashnet.org/experiments/cookie/.
The user should only launch the program.
It will start clicking the BigCookie and produce the cookies within 5 min (60 intervals of 5 sec).
After each 5 sec the program checks which upgrades are affordable, starting from the most expansive ones and purchase it.
It keeps on running being boosted with the upgrades.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Open the website with the game
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get all upgrades IDs
items = driver.find_elements(By.CSS_SELECTOR, "#store div")
items_id = [i.get_attribute("id") for i in items]
print(items_id)

# The function provides 60 cycles of 5 sec clicking on bigCookie:
cookie = driver.find_element(By.ID, 'cookie')
for cycle in range(0, 60):
    timeout = time.time() + 5  # 5 sec from now
    while True:
        cookie.click()
        if time.time() > timeout:
            break

    # Get money achieved in Integer after each 5 sec cycle
    money = driver.find_element(By.XPATH, value="/html/head/title").get_attribute("innerText")
    money_int = int(money.split()[0])

    # Get the list of all upgrade <b> tags (need to do it in the loop for ech next cycle as the prices get changed after each purchase)
    all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")

    # Get the prices for each item and change to Int:
    item_prices = [n.text.split("-")[-1].strip().replace(",", "") for n in all_prices]
    for price in item_prices:
        if price != "":
            price = int(price)
    # Print Prices Integer for process control
    print(item_prices)

    # Create the dictionary of UPGRADES and PRICES (Int)
    upgrades_dict = {}
    for n in range(0, len(items_id)):

        upgrades_dict[n] = {
            "upgrade": items_id[n],
            "price": item_prices[n],
        }
    # Print Upgrades:Prices dictionary for process control
    print(upgrades_dict)

    # Check for the most expensive upgrade available for purchase (the closer to the end of the list - the more expensive)
    for upgrade in range(len(items_id)-1, -1, -1):
        # using try except to catch the error caused by absence of the price for the last unit in the list from the site
        try:
            if money_int >= int(upgrades_dict[upgrade]["price"]):
                print(f"I will buy {upgrades_dict[upgrade]["upgrade"]}")
                driver.find_element(By.ID, value=upgrades_dict[upgrade]["upgrade"]).click()
                break
        except ValueError:
            pass

