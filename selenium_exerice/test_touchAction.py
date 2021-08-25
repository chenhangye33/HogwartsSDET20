from time import sleep

import pytest

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.keys import Keys


class TestTouchAction():
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.quit()



    def test_touchaction_scrollbottom(self):
        """
        打开Chrome
        打开URL：http://www.baidu.com
        向搜索框中输入'selenium测试'
        通过TouchAction点击搜索框
        滑动到底部，点击下一页
        关闭Chrome
        :return:
        """
        self.driver.get("http://www.baidu.com")
        ele = self.driver.find_element_by_xpath('//*[@id="kw"]')
        ele_search = self.driver.find_element_by_xpath('//*[@id="su"]')
        ele.send_keys("霍格沃兹测试学院")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele,0,10000).perform()
        # sleep(5)





