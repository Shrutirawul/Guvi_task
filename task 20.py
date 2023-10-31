# Using Selenium Automation and the URL "https://www.cowin.gov.in/" you have to :-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options
from time import sleep
import os
import requests

class Shruti:
    def __init__(self):
        self.url = "https://www.cowin.gov.in/"
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def questions(self):
        try:
            # 1) Click on FAQ and Partners anchor tags present on the Home Tab and open two new windows.
            # 2) Now , you have to fetch the Windows ID and display the same on the console.
            # 3) Kindly close the new windows and come back to the home page.
            self.driver.maximize_window()
            self.driver.get(self.url)
            self.driver.find_element(by=By.LINK_TEXT, value="FAQ").click()
            sleep(4)
        
            window_id = self.driver.current_window_handle
            print("Window ID of FAQ", window_id)
            self.driver.find_element(by=By.XPATH, value='//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[5]/a').click()
            sleep(10)
            window_handles = self.driver.window_handles
            window_id = self.driver.current_window_handle
            print("Window ID of Partners", window_id)
            
            # Switch to the second tab and close it if it exists
            if len(window_handles) > 1:
                self.driver.switch_to.window(window_handles[1])
                self.driver.close()
                sleep(4)
            
            # Switch to the first tab and close it
            self.driver.switch_to.window(window_handles[0])
            self.driver.close()
            sleep(4)
                   
        except NoSuchElementException as selenium_error:
            print(selenium_error)
        finally:
            self.driver.quit()
x = Shruti()
x.questions()

# Using Python Selenium visit the URL "https://labour.gov.in/" and do the following task:
# 1)Goto the Menu whose name is "Documents" and download the Monthly Progress Report.
# 2)Go to the Menu whose name is "Media" where there is a sub-menu "Photo Gallery".Your task is to download 10 photos from the webpage and store them in a folder
class Labour:
    def __init__(self):
        self.download_dir = "c:\\selenium-images"
        
        options = Options()
        options.set_preference("browser.download.folderList", 2)  # Set download directory
        options.set_preference("browser.download.manager.showWhenStarting", False)
        options.set_preference("browser.download.dir", self.download_dir)  # Specify the directory path
        options.set_preference("browser.download.useDownloadDir", True)
        options.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")  # Set MIME type for PDF
        options.set_preference("pdfjs.disabled", True)

        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)

    def create_folder(self):
        image_dir = os.path.join(self.download_dir, "images")
        os.makedirs(image_dir, exist_ok=True)


    def labour_document(self):
     
        self.driver.maximize_window()
        self.driver.get("https://labour.gov.in/")

        # Hover over the "Documents" link and click on "Monthly Reports"
        documents_link = self.driver.find_element(By.LINK_TEXT, "Documents")
        ActionChains(self.driver).move_to_element(documents_link).perform()

        self.driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/ul/li[2]/a').click()

        # Click on the PDF link
        self.driver.find_element(By.XPATH, '/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
        alert = self.driver.switch_to.alert
        alert.accept()

        # Wait for the download to complete (you might need to adjust the sleep time)
        sleep(5)
    
        print("pdf got downloaded")


    def labour_photos(self):
     
        media_link=self.driver.find_element(By.LINK_TEXT,"Media")
        ActionChains(self.driver).move_to_element(media_link).perform()
        sleep(5)
        self.driver.find_element(By.LINK_TEXT,"Photo Gallery").click()
        sleep(2)
        self.driver.find_element(By.XPATH,'/html/body/section[3]/div/div/div[3]/div[2]/div[1]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/div[2]/span/a').click()
        image_elements = self.driver.find_elements(By.XPATH,'//img[@typeof ="foaf:Image"]')[:10] 
        sleep(5)


        for index, image_element in enumerate(image_elements):
            image_url = image_element.get_attribute("src")
            if image_url:
                # Send a GET request to the image URL
                response = requests.get(image_url, stream=True)
                
                # Save the image to the 'images' directory using the full path
                image_dir = os.path.join(self.download_dir, "images")
                with open(os.path.join(image_dir, f"image{index}.png"), "wb") as img_file:
                    img_file.write(response.content)
                
        
        self.driver.quit()
        



shruti = Labour()
shruti.create_folder()
shruti.labour_document()
shruti.labour_photos()
