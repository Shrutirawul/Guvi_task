#Using Selenium Python,Excplicit Wait,Explicit Conditions and with Chrome Webdriver kindly do the task
# Using the given URL fill the input box,Select box and drop down on the webpage
# do not use sleep()

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class Shruti:
    def __init__(self):
        self.url = "https://www.imdb.com/search/name/"
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def film_search(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)

            # Scroll down
            self.driver.execute_script("window.scrollBy(0, 720);")

            # Wait for the 'Expand all' button to be clickable
            expand_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="__next"]/main/div[2]/div[3]/section/section/div/section/section/div[2]/div/section/div[2]/div[1]/div/button/span'))
            )
            expand_button.click()

            # Wait for the search input field to be present and visible
            search_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "text-input__5863"))
            )
            search_input.send_keys("five")

            # Wait for the birth date button 1 to be present and visible
            birth_date_button1 = self.wait.until(
                EC.presence_of_element_located((By.ID, "text-input__255"))
            )
            birth_date_button1.clear()
            birth_date_button1.send_keys("01012022")

            # Wait for the birth date button 2 to be present and visible
            birth_date_button2 = self.wait.until(
                EC.presence_of_element_located((By.ID, "text-input__256"))
            )
            birth_date_button2.clear()
            birth_date_button2.send_keys("10102022")

            # Wait for the birth month field to be present and visible
            birth_month = self.wait.until(EC.presence_of_element_located((By.ID, "text-input__257")))
            
            birth_month.clear()
            birth_month.send_keys("02-15")
            birth_month.send_keys(Keys.ENTER)

        except TimeoutException as e:
            print(f"TimeoutException: {e}")

        finally:
            self.driver.quit()

# Create an instance and call the method
x = Shruti()
x.film_search()
