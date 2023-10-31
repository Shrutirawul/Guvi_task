from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

class Shruti:
    def __init__(self):
        self.url = "https://jqueryui.com/droppable/"
        self.driver  = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def drag_drop(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            
            iframe = self.driver.find_element(By.CSS_SELECTOR,'.demo-frame')
            self.driver.switch_to.frame(iframe)
            sleep(3)
            source = self.driver.find_element(By.ID, "draggable")
            destination = self.driver.find_element(By.ID, "droppable")
            
            action_chains = ActionChains(self.driver)
            action_chains.drag_and_drop(source, destination).perform()
            sleep(3)
            print("Dropped")
        finally:
            self.driver.quit()

x = Shruti()
x.drag_drop()
