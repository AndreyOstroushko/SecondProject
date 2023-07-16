from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

class News_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators
    massage_button = '//li[@id="l_msg"]'

#Getters
    def get_massage_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.massage_button)))

#Actions
    def click_massage_button(self):
        self.get_massage_button().click()

    def massage(self):
        self.click_massage_button()