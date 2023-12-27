class Shruti:
    def __init__(self):
        self.driver = None
        self.wait = None  # Initialize wait attribute

    def orange(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get(locators.test_locators1().url)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 15)  # Initialize wait object

    def reset_password(self):
        try:
            print("Resetting password...")

            self.driver.find_element(by=By.XPATH, value=locators.test_locators1().forgot_your_password).click()
            self.driver.find_element(by=By.NAME, value=locators.test_locators1().username_name).send_keys(data.test_data1().username)
            self.driver.find_element(by=By.XPATH, value=locators.test_locators1().reset_password).click()

            # Wait for the element to be present in the DOM before checking for visibility
            expected_result = self.wait.until(
                EC.presence_of_element_located((By.XPATH, locators.test_locators1().reset_msg))
            ).text

            actual_data = "Reset Password link sent successfully"
            
            if actual_data == expected_result:
                print("Reset Password link sent successfully")
            else:
                print("Could not reset the password. Actual: {}, Expected: {}".format(actual_data, expected_result))
            
        except NoSuchElementException as e:
            print("Element not found: ", e)
        except TimeoutException as e:
            print("Timeout waiting for element: ", e)
        except Exception as e:
            print("Error: ", e)
        finally:
            self.driver.quit()

x = Shruti()
x.orange()
x.reset_password()