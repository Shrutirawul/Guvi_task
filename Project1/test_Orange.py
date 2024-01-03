import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from test_locators import locators
from test_data import excel_functions
from test_data import data1
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait


class TestOrangeManager:
    
    @pytest.fixture
    def setup(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(locators.Test_Locators().url)
        self.driver.implicitly_wait(15)
        self.wait = WebDriverWait(self.driver, 40)
        yield
        self.driver.quit()
      
    def test_login(self, setup):
        username = s.read_data(2, 6)
        password = s.read_data(2, 7)
        
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().username_locator).send_keys(username)
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().password_locator).send_keys(password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().submit_button).click()

        self.driver.implicitly_wait(10)

        dashboard_url = locators.Test_Locators().dash_url

        if dashboard_url in self.driver.current_url:
            print(f"SUCCESS : Login success with username {username}")
            s.write_data(2, 8, "TEST PASS")
            self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().logout_drop_xpath).click()
            self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().logout_xpath).click()
            self.driver.refresh()
        else:
            print(f"FAIL : Login failure with username {username}")
            s.write_data(2, 8, "TEST FAIL")
            self.driver.refresh()

    def test_login_2(self, setup):
        username = s.read_data(3, 6)
        password = s.read_data(3, 7)

        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().username_locator).send_keys(username)
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().password_locator).send_keys(password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().submit_button).click()

        self.driver.implicitly_wait(10)

        dashboard_url = locators.Test_Locators().dash_url
    
        if dashboard_url in self.driver.current_url:
            print(f"SUCCESS : Login success with username {username}")
            s.write_data(3, 8, "TEST PASS")
            self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().logout_drop_xpath).click()
            self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().logout_xpath).click()
            self.driver.refresh()
        else:
            print(f"FAIL : Login failure")
            s.write_data(3, 8, "TEST FAIL")
            self.driver.refresh()

    def test_add__edit_delete_employee(self, setup):
        # to add new employee
        username = s.read_data(4, 6)
        password = s.read_data(4, 7)

        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().username_locator).send_keys(username)
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().password_locator).send_keys(password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().submit_button).click()

        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().pim_xpath).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().add_xpath).click()

        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().first_name).send_keys(data1.Orange_Data().first_name)
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().middle_name).send_keys(data1.Orange_Data().middle_name)
        self.driver.find_element(by=By.NAME, value=locators.Test_Locators().last_name).send_keys(data1.Orange_Data().last_name)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().creditials).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().login_username).send_keys(data1.Orange_Data().login_username)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().login_password).send_keys(data1.Orange_Data().login_password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().confirm_password).send_keys(data1.Orange_Data().confirm_password)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().save_button).click()

        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().nickname).send_keys(data1.Orange_Data().nickname)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().driving_license).send_keys(data1.Orange_Data().driving_license)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().SSN).send_keys(data1.Orange_Data().SSN)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().SIN).send_keys(data1.Orange_Data().SIN)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().Nationality).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().Martial_status).click()
        self.driver.execute_script(f"arguments[0].value = '{data1.Orange_Data().DOB}';", locators.Test_Locators().DOB)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().Military).send_keys(data1.Orange_Data().military)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().save_button1).click()


        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().employee_list).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().employee_name).send_keys(data1.Orange_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().search).click()


        search_record1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.Test_Locators().record_data)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_record1)

        search = data1.Orange_Data().record_name

        if search_record1.text in search:
            assert search_record1.text in search
            print("Search Record Found on: ", search_record1.text)
            s.write_data(4, 8, "TEST PASS")
        else:
             s.write_data(4, 8, "TEST FAIL")

        #  To Edit the Employee 
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().edit).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().other_id).send_keys(data1.Orange_Data().other_id)
        ssn_editable = self.driver.find_element(
            by=By.XPATH, value=locators.Test_Locators().SSN)
        ssn_editable.send_keys(Keys.BACKSPACE * len(ssn_editable.get_attribute("value")))
        ssn_editable.send_keys(data1.Orange_Data().edit_SSN)

        edited_value = ssn_editable.get_attribute("value")
        assert edited_value == data1.Orange_Data().edit_SSN
        print("Data Edited Successfully")
        
        if edited_value == data1.Orange_Data().edit_SSN:
            self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().save_button3).click()
            s.write_data(5, 8, "TEST PASS")
        else:
             s.write_data(5, 8, "TEST FAIL")

        

        # to delete an employee
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().employee_list).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().employee_name).send_keys(data1.Orange_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().search).click()
        search_record1 = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.Test_Locators().record_data)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", search_record1)
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().delete).click()
        self.driver.find_element(by=By.XPATH, value=locators.Test_Locators().delete1).click()


        no_record_display = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, locators.Test_Locators().no_record)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", no_record_display)

        assert no_record_display.is_displayed()
        exp_no_rec_data =data1.Orange_Data().expected_no_record
        if exp_no_rec_data in no_record_display.text:
            s.write_data(6, 8, "TEST PASS")
            print("Data Deleted Successfully")
        else:
            s.write_data(6, 8, "TEST FAIL")
            

# Set up Excel functions
excel_file = r"C:\Users\KK\Desktop\Guvi assignment\Project1\testdata.xlsx"
sheet_number = "Sheet1"
s = excel_functions.Suman_Excel_Functions(excel_file, sheet_number)
