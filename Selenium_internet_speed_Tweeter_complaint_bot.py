"""
Application name: Internet Speed Test and Automatic Tweet Creation

Technologies used: Selenium, speedtest.com, tweeter.com

Application Type: Selenium Utilization

Data of work start: 06 Jan 2024

Work finished: 07 Jan 2024

Application description:
The application is meant to support the user in communicating and defencing his rights in possible argues with his
internet providing company.
When launched, it contacts speedtest.com and in the case if the actual internet speed is lower than the one guaranteed
by the provider, it creates public post in Tweeter, addressing the following question to the internet providing company:
Hey, @Internet Provider, why is my speed xx down/xx up, when I pay for xx down/xx up?"

"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Input MIN speed guaranteed by the provider
PROMISED_DOWN = 150
PROMISED_UP = 100
PROVIDER = "Internet Provider"

# Input your Tweeter credentials
X_EMAIL = os.environ["X_EMAIL"]
X_PASSWORD = os.environ["X_PASSWORD"]


# I create the bot class
class InternetSpeedTwitterBot:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        # This function opens speedtest.net, rejects cookies and launch the test.
        self.driver.get("https://www.speedtest.net/")
        reject_button = self.driver.find_element(By.ID, value="onetrust-reject-all-handler")
        reject_button.click()
        go_button = self.driver.find_element(By.XPATH,
                                             value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go_button.click()

        # After 40 sec reads the speed results and returns them as function's result
        time.sleep(40)
        down_speed = self.driver.find_element(By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        up_speed = self.driver.find_element(By.XPATH,
                                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        if float(down_speed.text) < PROMISED_DOWN or float(up_speed.text) < PROMISED_UP:
            return (f"Hey, @{PROVIDER}, why is my speed {down_speed.text}down/{up_speed.text}up, "
                    f"when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?")
        else:
            exit(0)

    def tweet_at_provider(self):
        # After 2 sec delay for loading launch Tweeter login page
        time.sleep(2)
        self.driver.get('https://twitter.com/i/flow/login')

        # After 3 sec delay for loading input user email and press Next
        time.sleep(3)
        username = self.driver.find_element(By.NAME, value='text')

        # print(username.get_attribute("type"))
        username.send_keys(X_EMAIL)
        time.sleep(1)
        button_list = self.driver.find_elements(By.CSS_SELECTOR, value='div[role="button"]')
        button_list[2].click()

        # After 2 sec delay for loading input Password and press Sign in
        time.sleep(2)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(X_PASSWORD)
        button_list = self.driver.find_elements(By.CSS_SELECTOR, value='div[role="button"]')
        button_list[2].click()

        # After 3 sec delay for loading Reject cookies, launch the new Tweet
        # Then after another 2 sec insert the message text, formed from function 1 results and press Post
        time.sleep(3)
        reject_cookies = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div[2]/div[2]')
        reject_cookies.click()
        tweet_init = self.driver.find_element(By.XPATH,
                                              value='//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
        tweet_init.click()
        time.sleep(2)
        tweet_text = self.driver.find_element(By.CSS_SELECTOR, value='.DraftEditor-editorContainer div')
        tweet_text.send_keys(message)
        time.sleep(1)
        button_list = self.driver.find_elements(By.CSS_SELECTOR, value='div[role="button"]')
        button_list[12].click()


# Initialise Object and 2 methods
bot = InternetSpeedTwitterBot()
message = (bot.get_internet_speed())
bot.tweet_at_provider()
