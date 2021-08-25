from selenium import webdriver


class Testwait:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com")
    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("霍格沃兹测试学院")
