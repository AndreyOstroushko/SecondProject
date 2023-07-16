from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

class Password_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

#Locators
    password = '//input[@name="password"]'

#Getters
    def get_user_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

#Actions
    def input_user_password(self):
        self.get_user_password().send_keys('Djigit47')
        self.get_user_password().send_keys(Keys.RETURN)
        print('Input user password')


    def input_password(self):
        self.get_current_url()
        self.input_user_password()