from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

class Autorization_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators
    code = '//input[@name="otp"]'

#Getters
    def get_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.code)))

#Actions
    def input_code(self):
        self.get_code().send_keys(input())
        return self.get_code().send_keys(Keys.RETURN)


    def autorization_code(self):
        self.get_current_url()
        self.input_code()
