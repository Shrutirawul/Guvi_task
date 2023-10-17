from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class Instagram:

    def __init__(self,web_url):
        self.url = web_url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def insta_login(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(4)


            # Get the follower count element and print the number of followers
            follower_count_element = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
            follower_count = follower_count_element.text
            print("Number of followers:", follower_count)

            # Get the following count element and print the number of following
            following_count = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[3]/button')
            following_count = following_count.text
            print("Number of following:",following_count)
        
        except NoSuchElementException as selenium_error:
            print("Element Not Found",selenium_error)

        finally:
            self.driver.close()

url = "https://www.instagram.com/guviofficial/"
x = Instagram(url)
x.insta_login()














