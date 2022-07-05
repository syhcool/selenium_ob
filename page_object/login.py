# -*- coding:utf-8 -*-
# user:syh
from time import sleep

from selenium.webdriver.support.wait import WebDriverWait

from config.Conf import get_screenshot_path
from selenium import webdriver

class Login():
    def login(self,name='admin',password='1234561'):
        self.driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html')
        self.driver.maximize_window()
        self.driver.find_element_by_id('account').send_keys(name)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_id('submit').click()
        sleep(3)
        try:
            alert = self.driver.switch_to.alert
            if alert:
                return alert.text
                alert.accept()
        except:
            title = self.driver.title
            return title


if __name__ == "__main__":
    l = Login()
    l.login()