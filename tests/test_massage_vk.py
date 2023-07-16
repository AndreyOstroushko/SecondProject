from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base
from pages.autorization_page import Autorization_page
from pages.login_page import Login_page
from time import sleep

from pages.news_page import News_page
from pages.password_page import Password_page


def test_massage_vk():
    driver = webdriver.Chrome()
    print('Start Test')

    lp = Login_page(driver)
    lp.input_login()
    sleep(2)
    pp = Password_page(driver)
    pp.input_password()
    sleep(2)
    ca = Autorization_page(driver)
    ca.autorization_code()
    sleep(10)
    mbp = News_page(driver)
    mbp.massage()
    driver.quit()


