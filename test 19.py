# Visit the URL "https://www.saucedemo.com/" and login with the following credetials: Username = standard_user , Password = secret_user
# Try to fetch the following Python Selenium:
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
           self.driver.find_element(by=By.ID, value="user-name").send_keys(self.username)
           sleep(2)
           self.driver.find_element(by=By.ID, value="password").send_keys(self.password)
           self.driver.find_element(by=By.ID, value= "login-button").click()
           sleep(4)
# 1) To fetch the title of the Webpage
           print("The Title of the webpage is:",self.driver.title)
# 2) Curret URL of the webpage
           print("The current URL of the webpage is:",self.driver.current_url)
 # 3) To extract the entire contents of the webpage and save it in text file by name -Webpage_task_11
           f = open("Webpage_task_11.txt", "w")
           f.write(self.driver.find_element(By.XPATH, "/html/body").text)
           f.close()

       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
           self.driver.close()


url = "https://www.saucedemo.com/"
shruti = Shruti(url)
shruti.login()
