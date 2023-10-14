# Using the Selenium Python Automatio and the URL "https://www.saucedemo.com/" display the cookie created before login and after login in the console.

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException


class Shruti:
   username = "standard_user"
   password = "secret_sauce"
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))


   def login(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(4)
           cookies_before_login = self.driver.get_cookies()
           print("Cookies before login:")
           print(cookies_before_login)
           sleep(4)
           self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
           sleep(2)
           self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
           self.driver.find_element(by=By.ID, value= "login-button").click()
           sleep(4)
           cookies_after_login = self.driver.get_cookies()
           print("Cookies after login:")
           print(cookies_after_login)


       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
           self.driver.close()


url = "https://www.saucedemo.com/"
shruti = Shruti(url)
shruti.login()