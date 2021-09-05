from selenium import webdriver
from selenium.webdriver.common.by import By

from web.page_object.add_member_page import AddMemberPage
from web.page_object.base_page import BasePage
from web.page_object.contact_page import ContactPage

#IndexPage继承BasePage
class IndexPage(BasePage):
    def goto_add_member(self):
        """
        跳转添加成员页面
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".index_service_cnt_itemWrap").click()
        return AddMemberPage(self.driver)

    def goto_contact(self):
        """
        跳转通讯录
        ：return 返回contace页面实例对象
        :return:

        # A-> B A跳转 B页面，那么A这个方法的返回值就是B页面
        """
        return ContactPage(self.driver)
