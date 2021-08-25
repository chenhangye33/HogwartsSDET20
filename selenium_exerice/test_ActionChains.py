from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestActionChains():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
    def teardown(self):
        self.driver.quit()

    @pytest.mark.skip
    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        elemenet_click=self.driver.find_element_by_xpath("//input[@value='click me']")
        elemenet_doubleclick=self.driver.find_element_by_xpath("//input[@value='dbl click me']")
        elemenet_rightclick=self.driver.find_element_by_xpath("//input[@value='right click me']")
        action = ActionChains(self.driver)

        action.click(elemenet_click)
        action.context_click(elemenet_rightclick)
        action.double_click(elemenet_doubleclick)

        action.perform()


    def test_case_move(self):
        self.driver.get("http://www.baidu.com")
        #找设置元素
        ele = self.driver.find_element_by_id("s-usersetting-top")
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()
        sleep(5)

    @pytest.mark.skip
    def test_sendkeys(self):
        self.driver.get("https://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath("/html/body/label[1]/input")
        #光标移动到这个元素上，点击下
        ele.click()
        sleep(3)

        action = ActionChains(self.driver)
        #输入APPLE1,停1秒
        action.send_keys("APPLE1").pause(1)
        #输入空格，停1秒
        action.send_keys(Keys.SPACE).pause(1)
        #输入23，停1秒
        action.send_keys("23").pause(1)
        action.send_keys(Keys.BACK_SPACE).perform()
        sleep(3)
