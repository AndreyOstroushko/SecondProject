from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base

class Login_page(Base):
    base_url = 'https://vk.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


#Locators
    login = '//input[@name="login"]'

#Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login)))


#Actions
    def input_user_name(self):
        self.get_user_name().send_keys('79654722781')
        self.get_user_name().send_keys(Keys.RETURN)
        print('Input user login')


    def input_login(self):
        self.driver.get(self.base_url)
        self.driver.maximize_window()
        self.input_user_name()
        self.get_current_url()
