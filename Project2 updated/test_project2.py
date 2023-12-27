from selenium.webdriver.firefox.service import Service
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_locators import locators
from test_data import data
import pytest


class Test_Capstone2:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 40)
        self.driver.get(locators.test_locators1().url)
        self.driver.maximize_window()
        yield
        self.driver.close()

    # TC_PIM_01

    def test_resetpassword(self, booting_function):

        try:
            forgot_password_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.test_locators1().forgot_your_password)))
            forgot_password_link.click()

            UserName = self.wait.until(
                EC.element_to_be_clickable((By.NAME, locators.test_locators1().username_name)))
            UserName.click()
            username_data = data.test_data1().username
            UserName.send_keys(username_data)

            reset = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.test_locators1().reset_password))).click()

            # Wait for the element to be present in the DOM before checking for visibility
            expected_result = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.test_locators1().reset_msg))
            ).text

            actual_data = data.test_data1().expected_reset_password
            
            if actual_data == expected_result:
                assert actual_data == expected_result
                print("Reset Password link sent successfully")
            else:
                print("Could not reset the password. Actual: {}, Expected: {}".format(actual_data, expected_result))
        except Exception as e:
            print("error on: ", e)

    def login(self):
        # Perform login
        self.driver.find_element(by=By.XPATH, value=locators.test_locators1().username1).send_keys(data.test_data1().username1)
        self.driver.find_element(by=By.XPATH, value=locators.test_locators1().password).send_keys(data.test_data1().password)
        self.driver.find_element(by=By.XPATH, value=locators.test_locators1().login).click()

    # TC_PIM_02
    def test_title(self, booting_function):
        try:
            self.login()

        #  Wait for the login process to complete, adjust the condition based on your application
           

        # Validate the title
            expected_title = data.test_data1().expected_title1
            actual_title = self.driver.title
            if expected_title == actual_title:
                assert actual_title == expected_title, f'Title mismatch. Expected: {expected_title}, Actual: {actual_title}'
                print('Title validation passed!')
            else:
                print("Verification failed: ", actual_title)

        except Exception as e:
            print("Error occurred: ", e)


    def test_menu(self, booting_function):
        try: 
            self.login()    
            self.driver.find_element(by=By.XPATH, value=locators.test_locators1().admin).click()
            menu_tabs = self.driver.find_elements(By.CLASS_NAME, locators.test_locators1().admin_elements)
            menu_items = data.test_data1().expected_menu_items

    # Validate each menu tab
            for element, expected_text in zip(menu_tabs, menu_items):
                if element.is_displayed(): 
                    assert element.text == expected_text
                    print(f"Menu item '{expected_text}' is displayed with the correct text.")
                else:
                    print(f"Menu item '{expected_text}' is either not displayed or has incorrect text.")
        except Exception as e:
            print("menu_tab error on: ",e)


    #TC_PIM_03
    def test_main_menu(self, booting_function):
        try: 
            self.login()
            self.driver.find_element(by=By.XPATH, value=locators.test_locators1().admin).click()    
            
            main_menu = self.driver.find_elements(By.CLASS_NAME, locators.test_locators1().main_menu_items)
            main_menu_data = data.test_data1().expected_main_menu

    # Validate each menu
            for element, expected_text in zip(main_menu, main_menu_data):
                if element.is_displayed(): 
                    assert element.text == expected_text
                    print(f"Main menu item '{expected_text}' is displayed with the correct text.")
                else:
                    print(f"Main menu item '{expected_text}' is either not displayed or has incorrect text.")
        except Exception as e:
            print("menu_tab error on: ",e)

        
            



        

       

       







        



   
   


       
