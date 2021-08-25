import selenium
from  selenium import webdriver
from selenium.webdriver.common.by import By


class Testselenium():
    def setup(self):
        #初始化driver
       self.driver = webdriver.Chrome()
        #显式等待
       self.driver.implicitly_wait(3)
       self.driver.get("https://www.baidu.com")

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element(By.ID,'su').click()
        self.driver.find_elements_by_link_text('Python 基础教程 | 菜鸟教程')

